from langchain_community.document_loaders import GithubFileLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import asyncio
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

Ask me about any code, and I'll provide simple, understandable documentation.
"""

# Fetch GitHub docs
loader = GithubFileLoader(
    repo="ifsvivek/CodeDocGenAI",
    branch="main",
    access_token=access_token,
    github_api_url="https://api.github.com",
    file_filter=lambda file_path: file_path.endswith(
        (".md", ".py", ".js", ".ts", ".c", ".cpp", ".java")
    ),
)
documents = loader.load()

# Combine base prompt with GitHub docs
system_prompt = (
    base_prompt
    + "\n\nGITHUB REPO INFO:\n"
    + "\n".join([doc.page_content for doc in documents])
)

# Initialize Groq chat
groq_chat = ChatGroq(
    groq_api_key=groq_api_key, model_name="llama-3.2-90b-vision-preview"
)

# Initialize conversation memory
conversation_memory[context_key] = ConversationBufferMemory(
    return_messages=True, memory_key="chat_history"
)


async def generate_response(prompt: str) -> str:
    prompt_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )

    # Create runnable sequence
    chain = prompt_template | groq_chat

    # Prepare the input with memory
    chat_history = conversation_memory[context_key].chat_memory.messages
    response = await chain.ainvoke(
        {"chat_history": chat_history, "human_input": prompt}
    )

    # Update memory
    conversation_memory[context_key].chat_memory.add_user_message(prompt)
    conversation_memory[context_key].chat_memory.add_ai_message(response.content)

    return response.content


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
