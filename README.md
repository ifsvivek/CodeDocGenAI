# CodeDocGenAI

**AI-Powered Code Documentation Generator**

CodeDocGenAI is an innovative tool that leverages artificial intelligence to generate clear, readable, and comprehensive documentation for GitHub repositories. Built with LangChain and Groq, it simplifies the process of understanding codebases for developers and non-technical users alike.

---

## 🚀 Key Features

-   **AI Documentation Generation**: Automatically creates clear and concise documentation from code.
-   **GitHub Integration**: Fetches repository contents, issues, and pull requests directly.
-   **Conversation Memory**: Maintains context during interactive documentation sessions.
-   **Multi-Format Support**: Supports multiple file types, including `.md`, `.py`, `.js`, `.ts`, `.c`, `.cpp`, and `.java`.

---

## 🛠️ Requirements

-   **Python**: Version 3.10 or higher
-   **GitHub Personal Access Token**: For accessing repositories ([Generate one here](https://github.com/settings/tokens?type=beta))
-   **Groq API Key**: For utilizing Groq-powered AI capabilities

---

## ⚙️ Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ifsvivek/CodeDocGenAI.git
    cd CodeDocGenAI
    ```

2. **Install dependencies**:

    ```bash
    pip install langchain-community langchain-groq python-dotenv
    ```

3. **Set up environment variables**:

    Create a `.env` file in the project root and add your credentials:

    ```
    ACCESS_TOKEN=your_github_token
    GROQ_API_KEY=your_groq_api_key
    ```

---

## 💻 Usage

Run the application:

```bash
python app.py
```

### Example Conversation

```
=== Code Documentation Generator AI ===
Type 'exit' to quit

You: Explain the main functions
AI: This codebase has two main functions:
- `generate_response`: Handles AI responses using Groq
- `main`: Runs the interactive CLI interface

You: exit
Goodbye!
```

---

## 📁 Project Structure

```
.
├── app.py         # Main application code
├── .env           # Environment variables
├── .gitignore     # Git ignore rules
└── README.md      # Project documentation
```

---

## 🔧 Configuration

The application requires the following environment variables:

-   **`ACCESS_TOKEN`**: Your GitHub Personal Access Token
-   **`GROQ_API_KEY`**: Your Groq API Key

Add these to a `.env` file in the root directory as shown in the installation steps.

---

## 🧑‍💻 Authors

-   **Vivek** - [GitHub Profile](https://github.com/ifsvivek)
-   **Yuvan** - [GitHub Profile](https://github.com/yuvan0309)

---

## 💬 Support

For any questions or issues, feel free to [open an issue](https://github.com/ifsvivek/CodeDocGenAI/issues) or reach out via email.
