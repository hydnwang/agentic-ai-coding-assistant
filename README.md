# AI Agent Demo 02: Coding Assistant

This project is a demonstration of an agentic AI coding assistant with a tool-calling design. The agent uses Google's Gemini model to intelligently call various tools to interact with a filesystem and execute Python code.

## 1. Features

-   **Agentic Loop**: Automatically performs multiple steps (up to 20 iterations) to solve complex user requests.
-   **Intelligent Tool Selection**: Uses Gemini-powered tool-calling to select the right function for the task.
-   **Secure File Operations**: Read, list, and write files within a designated `./calculator` directory.
-   **Dynamic Python Execution**: Execute Python scripts and capture their standard output.
-   **Conversation Persistence**: Maintains the chat history and the results of functional operations throughout the agentic process.
-   **Verbose Logging**: Optional detailed output including token usage and step-by-step function execution details.

## 2. Tech Stack

-   **Language**: Python 3.12+
-   **LLM SDK**: [google-genai](https://pypi.org/project/google-genai/) (Gemini 2.5 Flash)
-   **Dependency Management**: [uv](https://github.com/astral-sh/uv)
-   **Environment Configuration**: `python-dotenv`
-   **CLI Framework**: `argparse`

## 3. Project Structure

```text
.
├── main.py                 # Entry point: handles the AI agent loop and conversation
├── functions/              # Tool implementations
│   ├── call_function.py    # Function router and Gemini tool schema definitions
│   ├── get_file_content.py # Tool: Read a file's content
│   ├── get_files_info.py   # Tool: List files and directory information
│   ├── run_python_file.py  # Tool: Execute a Python script
│   └── write_file.py       # Tool: Create or update a file
├── calculator/             # Sandbox directory for agent operations
├── configs/                # System prompts and model configurations
├── .env                    # Environment variables (GEMINI_API_KEY)
├── pyproject.toml          # UV project configuration and dependencies
└── README.md               # Project documentation
```

## 4. Setup

1.  **Clone the repository** (if you haven't already).
2.  **Install `uv`**: Follow the instructions at [astral.sh/uv](https://astral.sh/uv).
3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your Gemini API Key:
    ```bash
    GEMINI_API_KEY=your_gemini_api_key_here
    ```
4.  **Install dependencies**:
    ```bash
    uv sync
    ```

## 5. Usage

To interact with the agent, run `main.py` using `uv` with your prompt:

```bash
uv run main.py "your core instruction or question here"
```

### Options
-   `--verbose`: Enable detailed output of token usage and internal tool-calling steps.

### Example
```bash
uv run main.py "Analyze the files in the calculator directory and create a new file named summary.txt describing what they do." --verbose
```
