# CodeDocGenAI

**AI-Powered Code Documentation Generator**

CodeDocGenAI is an innovative tool that leverages artificial intelligence to generate clear, readable, and comprehensive documentation for GitHub repositories. Built with LangChain and Groq's LLM API, it simplifies the process of understanding codebases for developers and non-technical users alike.

---

## 🚀 Key Features

-   **AI Documentation Generation**:

    -   Automatically generates clear and concise documentation from code
    -   Extracts key functional details and code structure
    -   Provides high-level overviews and detailed explanations
    -   Maintains documentation context across conversations

-   **GitHub Integration**:

    -   Seamlessly fetches repository contents using GitHub API
    -   Supports multiple file formats
    -   Handles repository analysis and content extraction
    -   Can process both public and private repositories

-   **Conversation Memory**:

    -   Maintains context during interactive documentation sessions
    -   Remembers previous queries and responses
    -   Allows for follow-up questions and deep-dive discussions
    -   Supports conversation reset functionality

-   **Multi-Format Support**:
    -   Markdown (.md) - Documentation and README files
    -   Python (.py) - Python source code
    -   JavaScript/TypeScript (.js, .ts) - Web application code
    -   C/C++ (.c, .cpp) - Systems programming code
    -   Java (.java) - Java applications

---

## 🛠️ Requirements

-   **Python**:

    -   Version 3.10 or higher required
    -   Async/await support for efficient API handling
    -   Modern language features utilized

-   **GitHub Personal Access Token**:

    -   Required for repository access
    -   Needs repo and read:org scopes
    -   Generate at [GitHub Token Settings](https://github.com/settings/tokens?type=beta)

-   **Groq API Key**:

    -   Powers the AI capabilities
    -   Used for natural language processing
    -   Handles code analysis and documentation generation

-   **Dependencies**:
    -   langchain-community: For GitHub integration
    -   langchain-groq: For AI model integration
    -   python-dotenv: For environment variable management

---

## ⚙️ Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ifsvivek/CodeDocGenAI.git
    cd CodeDocGenAI
    ```

2. **Set up virtual environment (recommended)**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install langchain-community langchain-groq python-dotenv
    ```

4. **Configure environment**:
   Create file with required credentials:
    ```
    ACCESS_TOKEN=your_github_token
    GROQ_API_KEY=your_groq_api_key
    ```

---

## 💻 Usage

1. **Start the application**:

    ```bash
    python app.py
    ```

2. **Basic commands**:

    - `exit`: Quit the application
    - `reset`: Clear conversation history and loaded repositories
    - Enter repository name (e.g., "ifsvivek/CodeDocGenAI") to analyze

3. **Example workflows**:

    ```
    === Code Documentation Generator AI ===
    You: analyze ifsvivek/CodeDocGenAI
    AI: Loading repository...
        Generated documentation for 3 files...

    You: explain the main functions
    AI: The codebase has these key functions:
        - generate_response: AI-powered response generation
        - load_github_repo: Repository content loading
        - handle_tool_call: Tool execution handling
        - main: CLI interface management
    ```

---

## 🧰 Core Components

1. **AI Integration**:

    - Uses Groq's LLM for natural language processing
    - Implements conversation memory for context retention
    - Supports tool-based operations for repository analysis

2. **GitHub Integration**:

    - GithubFileLoader for repository content access
    - Supports multiple file formats
    - Handles authentication and API interactions

3. **Memory Management**:

    - ConversationBufferMemory for chat history
    - Maintains context across queries
    - Supports conversation reset

4. **Tool System**:
    - XML-based tool definitions
    - Extensible tool architecture
    - Built-in repository loading capabilities

---

## 🔧 Configuration

**Environment Variables**:

-   `ACCESS_TOKEN`: GitHub Personal Access Token

    -   Required for repository access
    -   Must have appropriate repository access scopes

-   `GROQ_API_KEY`: Groq API Key
    -   Powers the AI functionality
    -   Rate limits apply based on your plan

**File Support**:

-   Documentation: .md
-   Code: .py, .js, .ts, .c, .cpp, .java
-   Configuration: .env, .gitignore

---

## 🧑‍💻 Authors

-   **Vivek** - [GitHub Profile](https://github.com/ifsvivek)

    -   Core development
    -   AI integration
    -   Documentation

-   **Yuvan** - [GitHub Profile](https://github.com/yuvan0309)
    -   Testing
    -   Bug fixes
    -   Feature implementation

---

## 💬 Support

-   **Issues**: [Open an issue](https://github.com/ifsvivek/CodeDocGenAI/issues)
-   **Discussions**: Use GitHub Discussions for questions
-   **Email**: Contact authors directly
-   **Documentation**: Refer to this README and inline code comments
