"""
Configuration file for AI Code Assistant.
Contains API keys and other sensitive configuration.
"""

# Groq API Configuration
GROQ_API_KEY = "Hidden_because_of_Zeeshan "

# Application Configuration
APP_NAME = "AI Code Assistant"
APP_VERSION = "1.0.0"

# Groq Models Configuration
AVAILABLE_MODELS = {
    "Llama 3.1 8B": "llama-3.1-8b-instant",
    "Llama 3.1 70B": "llama-3.1-70b-versatile", 
    "Mixtral 8x7B": "mixtral-8x7b-32768"
}

# API Settings
DEFAULT_TEMPERATURE = 0.3
MAX_TOKENS = 2000
