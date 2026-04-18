# AI Code Assistant

A Streamlit web application that provides AI-powered assistance for code-related tasks using Groq API.

## Features

- **Error Fixing**: Debug and fix code issues with AI assistance
- **Code Improvement**: Enhance code quality, readability, and performance
- **Code Generation**: Generate new code from requirements
- **Multiple AI Models**: Choose from 3 Groq models (Llama 3.1 8B, Llama 3.1 70B, Mixtral 8x7B)
- **Interactive UI**: Clean, intuitive interface with quick suggestions

## Project Structure

```
chatbot_najam/
├── main.py              # Streamlit entry point
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── modules/            # Application modules
    ├── groq_client.py  # Groq API integration
    └── ui_helpers.py   # UI helper functions
```

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Quick Start (Windows)

Run the provided batch file:
```bash
run_app.bat
```

Or use the PowerShell script:
```powershell
.\run_app.ps1
```

### 5. Set Up Groq API Key

Get your API key from [groq.com](https://groq.com) and set it up using one of these methods:

#### Option A: Environment Variable
```bash
export GROQ_API_KEY="your_api_key_here"
```

#### Option B: Streamlit Secrets
Create a `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your_api_key_here"
```

## Usage

1. **Start the application**:
   ```bash
   streamlit run main.py
   ```

2. **Select a mode**: Choose between Fix Error, Improve Code, or Generate Code

3. **Choose an AI model**: Select from available Groq models

4. **Input your code/prompt**: Provide the content you want to work with

5. **Get AI assistance**: Receive corrected/improved/generated code with explanations

## Available AI Models

- **Llama 3.1 8B**: Fast and efficient for quick tasks
- **Llama 3.1 70B**: More capable for complex tasks
- **Mixtral 8x7B**: Balanced performance and capabilities

## Quick Suggestions

The app provides quick suggestion buttons based on the selected mode:

- **Fix Error**: Syntax Error, Logic Error, Runtime Error
- **Improve Code**: Performance, Readability, Best Practices
- **Generate Code**: Function, Class, API Endpoint

## Architecture

The application follows a modular architecture with:

- **Low coupling**: Modules are independent and reusable
- **High cohesion**: Each module has a single, well-defined responsibility
- **Separation of concerns**: UI logic, API integration, and business logic are separated

### Module Descriptions

- **`groq_client.py`**: Handles all Groq API interactions
- **`ui_helpers.py`**: Contains reusable UI components and helpers
- **`main.py`**: Main application entry point and orchestration

## Development

To extend the application:

1. Add new modes in `groq_client.py` by updating the `_create_prompt` method
2. Add new UI components in `ui_helpers.py`
3. Update the main application flow in `main.py`

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your Groq API key is properly set
2. **Import Errors**: Ensure all dependencies are installed
3. **Model Not Available**: Check if the selected model is available in your region

### Getting Help

If you encounter issues:

1. Check the error messages in the application
2. Verify your API key setup
3. Ensure all dependencies are correctly installed
4. Check your internet connection for API access
