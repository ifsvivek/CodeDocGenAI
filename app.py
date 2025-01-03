import os, json, asyncio
from langchain_community.document_loaders import GithubFileLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)
from langchain.memory import ConversationBufferMemory

# Load environment variables
load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize variables
conversation_memory = {}
context_key = "default"
loaded_repos = {}

base_prompt = """
I am an AI documentation assistant specialized in analyzing GitHub codebases.
My primary functions:
- Analyze code to extract key functional details
- Generate clear, comprehensive documentation in simple English
- Support documentation for multiple programming languages
- Process GitHub repository contents effectively

Documentation style:
- Clear and concise explanations
- Focus on code purpose and functionality
- Avoid technical jargon where possible
- Highlight main components and their interactions

I provide documentation that helps users understand:
- What the code does
- How different parts work together
- Key features and functionalities
- Basic usage patterns

I use tools to help me. These tools are defined within <tools></tools> XML tags. When I need to use a tool, I'll call it like this:

<tool_call>
{"name": "<function-name>", "arguments": {"arg1": "value1", "arg2": "value2"}}
</tool_call>

Available tools:
- load_github_repo: Loads a GitHub repository for analysis
  Arguments: {"repo": "owner/repo", "branch": "branch_name"}
- reset_repos: Clears all loaded repositories
  Arguments: {}

Ask me about any code, and I'll provide simple, understandable documentation.
"""

# Initialize Groq chat
groq_chat = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")


async def load_github_repo(repo: str, branch: str = "main") -> str:
    try:
        loader = GithubFileLoader(
            repo=repo,
            branch=branch,
            access_token=access_token,
            github_api_url="https://api.github.com",
            file_filter=lambda file_path: file_path.endswith(
                (".md", ".py", ".js", ".ts", ".c", ".cpp", ".java")
            ),
        )
        documents = loader.load()
        loaded_repos[repo] = documents
        return f"Successfully loaded {len(documents)} files from {repo}"
    except Exception as e:
        return f"Error loading repository: {str(e)}"


async def reset_repos() -> str:
    try:
        loaded_repos.clear()
        return "Successfully cleared all loaded repositories"
    except Exception as e:
        return f"Error clearing repositories: {str(e)}"


async def handle_tool_call(response, memory):
    start = response.index("<tool_call>") + len("<tool_call>")
    end = response.index("</tool_call>")
    tool_call_json = response[start:end].strip()

    try:
        tool_call = json.loads(tool_call_json)
        tool_name = tool_call.get("name")
        tool_arguments = tool_call.get("arguments", {})
        result = None

        tool_actions = {
            "load_github_repo": lambda: load_github_repo(
                tool_arguments.get("repo"), tool_arguments.get("branch", "main")
            ),
            "reset_repos": reset_repos,
        }

        action = tool_actions.get(tool_name)
        if action:
            result = await action()
        else:
            result = "Tool not found."

        if result is not None:
            memory.chat_memory.messages[-1].content += f"\nResult: {result}"
    except Exception as e:
        memory.chat_memory.messages[-1].content += f"\nError: {str(e)}"

    return memory.chat_memory.messages[-1].content


async def generate_response(prompt: str) -> str:
    # Get repo context if available
    repo_context = "\n".join(
        [
            f"\nRepo: {repo}\n" + "\n".join([doc.page_content for doc in docs])
            for repo, docs in loaded_repos.items()
        ]
    )

    system_prompt = base_prompt + repo_context

    prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )

    chain = prompt_template | groq_chat
    chat_history = conversation_memory[context_key].chat_memory.messages
    response = await chain.ainvoke(
        {"chat_history": chat_history, "human_input": prompt}
    )

    content = response.content

    # Handle tool calls if present
    if "<tool_call>" in content and "</tool_call>" in content:
        content = await handle_tool_call(content, conversation_memory[context_key])

    conversation_memory[context_key].chat_memory.add_user_message(prompt)
    conversation_memory[context_key].chat_memory.add_ai_message(content)

    return content


# Initialize conversation memory
conversation_memory[context_key] = ConversationBufferMemory(
    return_messages=True, memory_key="chat_history"
)


async def main():
    print("\n=== Code Documentation Generator AI ===")
    print("Type 'exit' to quit\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            if not user_input:
                continue

            response = await generate_response(user_input)
            print("\nAI:", response, "\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}\n")


if __name__ == "__main__":
    asyncio.run(main())
