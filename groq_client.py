"""
Groq API client module for AI assistant functionality.
Handles communication with Groq API for code-related tasks.
"""

import os
from typing import Dict, List, Optional
from groq import Groq
import streamlit as st

# Import configuration
try:
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    import config
except ImportError:
    config = None


class GroqClient:
    """Client for interacting with Groq API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize Groq client with API key."""
        # Priority: passed parameter -> config file -> environment variable -> Streamlit secrets
        self.api_key = (
            api_key or 
            (config.GROQ_API_KEY if config and hasattr(config, 'GROQ_API_KEY') else None) or
            os.getenv("GROQ_API_KEY") or
            st.secrets.get("GROQ_API_KEY")
        )
        
        if not self.api_key:
            raise ValueError("Groq API key is required. Set it in config.py, environment variable, or Streamlit secrets.")
        
        self.client = Groq(api_key=self.api_key)
        
        # Available models from config
        if config and hasattr(config, 'AVAILABLE_MODELS'):
            self.models = config.AVAILABLE_MODELS
        else:
            # Fallback models
            self.models = {
                "Llama 3.1 8B": "llama-3.1-8b-instant",
                "Llama 3.1 70B": "llama-3.1-70b-versatile", 
                "Mixtral 8x7B": "mixtral-8x7b-32768"
            }
    
    def get_available_models(self) -> List[str]:
        """Get list of available model names."""
        return list(self.models.keys())
    
    def _create_prompt(self, mode: str, code: str, additional_context: str = "") -> str:
        """Create appropriate prompt based on the selected mode."""
        if mode == "Fix Error":
            prompt = f"""You are an expert debugging assistant. Analyze the following code and identify any errors. 
Provide the corrected code and explain what was wrong and how you fixed it.

Code to debug:
```python
{code}
```

{additional_context}

Please provide:
1. The corrected code
2. A clear explanation of the errors found
3. How the fixes resolve the issues"""
        
        elif mode == "Improve Code":
            prompt = f"""You are an expert code reviewer and optimizer. Analyze the following code and suggest improvements.
Focus on readability, performance, best practices, and maintainability.

Code to improve:
```python
{code}
```

{additional_context}

Please provide:
1. The improved version of the code
2. A detailed explanation of the improvements made
3. The benefits of these changes"""
        
        elif mode == "Generate Code":
            prompt = f"""You are an expert software developer. Generate high-quality code based on the following requirements.

Requirements:
{code}

{additional_context}

Please provide:
1. The generated code
2. A clear explanation of how the code works
3. Any important notes about usage or dependencies"""
        
        else:
            raise ValueError(f"Unknown mode: {mode}")
        
        return prompt
    
    def get_response(self, mode: str, code: str, model_name: str, additional_context: str = "") -> Dict[str, str]:
        """Get AI response from Groq API."""
        if model_name not in self.models:
            raise ValueError(f"Model {model_name} not available. Choose from: {list(self.models.keys())}")
        
        model_id = self.models[model_name]
        prompt = self._create_prompt(mode, code, additional_context)
        
        try:
            response = self.client.chat.completions.create(
                model=model_id,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant specialized in code-related tasks."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            return {
                "success": True,
                "response": response.choices[0].message.content,
                "model_used": model_name
            }
            
        except Exception as e:
            error_msg = str(e)
            # Provide more helpful error messages for common issues
            if "organization_restricted" in error_msg:
                error_msg = "Your Groq API key has organization restrictions. Please get a new API key from console.groq.com"
            elif "invalid_request_error" in error_msg:
                error_msg = "Invalid API request. Please check your API key and try again."
            elif "authentication" in error_msg.lower():
                error_msg = "Authentication failed. Please check your API key configuration."
            
            return {
                "success": False,
                "error": error_msg,
                "model_used": model_name
            }


def initialize_groq_client() -> GroqClient:
    """Initialize and return Groq client, handling API key from Streamlit secrets."""
    try:
        # Try to get API key from Streamlit secrets first
        api_key = st.secrets.get("GROQ_API_KEY")
        return GroqClient(api_key=api_key)
    except Exception:
        # Fallback to environment variable
        return GroqClient()
