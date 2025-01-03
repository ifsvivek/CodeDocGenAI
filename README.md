# CodeDocGenAI

**Simplify Code Understanding with AI-Generated Documentation**

Welcome to **CodeDocGenAI**, an innovative tool designed to generate simple, clear, and comprehensive documentation for small to medium open-source codebases hosted on GitHub. Built with LangChain and Groq, this project empowers developers and non-technical users to understand the functionality and purpose of codebases more effectively.

## 🚀 Features

-   **AI-Powered Code Analysis**: Extracts functional details and insights from codebases.
-   **Multi-Language Support**: Handles a variety of programming languages to cater to diverse needs.
-   **Seamless GitHub Integration**: Load issues, pull requests, and file contents from GitHub repositories with ease.
-   **Readable Documentation**: Produces simple, user-friendly documentation tailored for both developers and non-technical stakeholders.

## 📚 How It Works

1. **Load GitHub Issues and Pull Requests**: Use the `GitHubIssuesLoader` to retrieve issues and pull requests from repositories, filtered by criteria like creators, labels, or state.
2. **Fetch Repository File Contents**: Leverage `GithubFileLoader` to fetch specific files (e.g., markdown files) for documentation generation.
3. **Generate Documentation**: Combine Groq and LangChain-powered models to create easy-to-understand documentation.

## 🔧 Technologies Used

-   **LangChain**: For advanced document loading and AI workflows.
-   **Groq**: To accelerate and optimize AI model performance.
-   **GitHub API**: To seamlessly interact with repositories.
-   **Python**: Core language for development.

## 🛠️ Setup

### Prerequisites

-   Python 3.10+
-   A GitHub Personal Access Token ([Generate your token here](https://github.com/settings/tokens?type=beta))

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/ifsvivek/CodeDocGenAI.git
    cd CodeDocGenAI
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up your GitHub Access Token:
    - Option 1: Set it as an environment variable:
        ```bash
        export GITHUB_PERSONAL_ACCESS_TOKEN=your_token_here
        ```
    - Option 2: Pass it directly in the scripts (not recommended for production).

### Usage

#### Load Issues and PRs

```python
from langchain_community.document_loaders import GitHubIssuesLoader

loader = GitHubIssuesLoader(
    repo="your-repo/your-repository",
    access_token="your_token_here",
    creator="your-github-username"
)
docs = loader.load()
print(docs[0].page_content)
```

#### Load File Contents

```python
from langchain_community.document_loaders import GithubFileLoader

loader = GithubFileLoader(
    repo="your-repo/your-repository",
    branch="main",
    access_token="your_token_here",
    file_filter=lambda file_path: file_path.endswith(".md")
)
documents = loader.load()
print(documents[0].content)
```

## 📅 Hackathon Timeline

-   **Submission Deadline**: January 8th, 2025
-   **Final Presentation**: January 28th, 2025 (15 minutes including demo and Q&A)

## 🏆 Goals for the Hackathon

-   Simplify and streamline documentation processes.
-   Enhance developer productivity and onboarding experience.
-   Demonstrate innovation using AI in real-world challenges.

## 💬 Questions or Feedback?

Feel free to reach out via [GitHub Issues](https://github.com/ifsvivek/CodeDocGenAI/issues) or email us.

---

We look forward to simplifying code documentation and helping you win this exciting hackathon!
