# CodeDocGenAI

**AI-Powered Code Documentation Generator**

CodeDocGenAI is a tool that uses artificial intelligence to automatically generate clear, readable documentation for GitHub repositories. Built with LangChain and Groq, it helps developers and users better understand codebases.

## 🚀 Key Features

-   **AI Documentation Generation**: Creates clear, concise documentation from code
-   **GitHub Integration**: Directly fetches repository contents and issues
-   **Conversation Memory**: Maintains context during documentation sessions
-   **Multi-Format Support**: Handles multiple file types (.md, .py, etc.)

## 🛠️ Requirements

-   Python 3.10+
-   GitHub Personal Access Token
-   Groq API Key

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/ifsvivek/CodeDocGenAI.git
cd CodeDocGenAI
```

2. Install dependencies:

```bash
pip install langchain-community langchain-groq python-dotenv
```

3. Create a `.env` file:

```
ACCESS_TOKEN=your_github_token
GROQ_API_KEY=your_groq_api_key
```

## 💻 Usage

Run the application:

```bash
python app.py
```

Example conversation:

```
=== Code Documentation Generator AI ===
Type 'exit' to quit

You: Explain the main functions
AI: This codebase has two main functions:
- generate_response: Handles AI responses using Groq
- main: Runs the interactive CLI interface

You: exit
Goodbye!
```

## 📁 Project Structure

```
.
├── app.py         # Main application code
├── .env           # Environment variables
├── .gitignore     # Git ignore rules
└── README.md      # Documentation
```

## 🔧 Configuration

The application uses two key environment variables:

-   `ACCESS_TOKEN`: Your GitHub Personal Access Token
-   `GROQ_API_KEY`: Your Groq API Key
