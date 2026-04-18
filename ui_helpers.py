"""
UI helper functions for Streamlit application.
Contains reusable UI components and styling functions.
"""

import streamlit as st
from typing import List, Dict, Tuple


def setup_page_config():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="AI Code Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def render_header():
    """Render application header."""
    st.title("🤖 AI Code Assistant")
    st.markdown("---")
    st.markdown("Get help with error fixing, code improvement, and code generation powered by Groq AI.")


def render_mode_selection() -> str:
    """Render mode selection buttons and return selected mode."""
    st.subheader("🎯 Select Task Mode")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🐛 Fix Error", key="fix_error", use_container_width=True, type="primary"):
            st.session_state.mode = "Fix Error"
    
    with col2:
        if st.button("✨ Improve Code", key="improve_code", use_container_width=True):
            st.session_state.mode = "Improve Code"
    
    with col3:
        if st.button("🚀 Generate Code", key="generate_code", use_container_width=True):
            st.session_state.mode = "Generate Code"
    
    # Display current mode
    if hasattr(st.session_state, 'mode') and st.session_state.mode:
        st.info(f"Current Mode: **{st.session_state.mode}**")
        return st.session_state.mode
    
    return None


def render_model_selection(models: List[str]) -> str:
    """Render model selection dropdown."""
    st.subheader("🧠 Choose AI Model")
    
    # Check if models list is empty or None
    if not models:
        st.error("No models available. Please check your API configuration.")
        return None
    
    # Default to first model if none selected or if selected model is not in the list
    if 'selected_model' not in st.session_state or st.session_state.selected_model not in models:
        st.session_state.selected_model = models[0]
    
    selected_model = st.selectbox(
        "Select Model:",
        models,
        index=models.index(st.session_state.selected_model),
        key="model_selector"
    )
    
    st.session_state.selected_model = selected_model
    return selected_model


def render_code_input_area(mode: str) -> Tuple[str, str]:
    """Render code input area and additional context."""
    st.subheader("💻 Input Area")
    
    # Determine placeholder based on mode
    if mode == "Fix Error":
        code_placeholder = "Paste your code with errors here..."
        context_placeholder = "Optional: Describe the error you're experiencing..."
    elif mode == "Improve Code":
        code_placeholder = "Paste your code to improve here..."
        context_placeholder = "Optional: What specific improvements are you looking for?"
    else:  # Generate Code
        code_placeholder = "Describe what code you want to generate..."
        context_placeholder = "Optional: Any specific requirements or constraints?"
    
    # Code input
    code_input = st.text_area(
        "Code/Prompt:",
        placeholder=code_placeholder,
        height=200,
        key="code_input"
    )
    
    # Additional context
    additional_context = st.text_area(
        "Additional Context (Optional):",
        placeholder=context_placeholder,
        height=100,
        key="additional_context"
    )
    
    return code_input, additional_context


def render_quick_suggestions(mode: str) -> str:
    """Render quick suggestion buttons and return selected suggestion."""
    st.subheader("⚡ Quick Suggestions")
    
    suggestions = get_suggestions_for_mode(mode)
    
    selected_suggestion = ""
    cols = st.columns(len(suggestions))
    
    for i, suggestion in enumerate(suggestions):
        with cols[i]:
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                selected_suggestion = suggestion
    
    return selected_suggestion


def get_suggestions_for_mode(mode: str) -> List[str]:
    """Get quick suggestions based on the selected mode."""
    if mode == "Fix Error":
        return [
            "Syntax Error",
            "Logic Error", 
            "Runtime Error"
        ]
    elif mode == "Improve Code":
        return [
            "Performance",
            "Readability",
            "Best Practices"
        ]
    else:  # Generate Code
        return [
            "Function",
            "Class",
            "API Endpoint"
        ]


def render_submit_button() -> bool:
    """Render submit button and return if clicked."""
    return st.button("🚀 Submit", type="primary", use_container_width=True)


def render_response_area(response_data: Dict[str, str]):
    """Render the AI response area."""
    st.subheader("📝 AI Response")
    
    if response_data.get("success"):
        st.success(f"Response generated using **{response_data.get('model_used', 'Unknown')}**")
        
        response_text = response_data.get("response", "")
        
        # Display response with syntax highlighting for code blocks
        st.markdown(response_text)
        
        # Add copy button
        if st.button("📋 Copy Response", key="copy_response"):
            st.write("Response copied to clipboard!")
    else:
        st.error("❌ Error occurred while generating response")
        st.error(response_data.get("error", "Unknown error"))


def render_sidebar_info():
    """Render sidebar information and tips."""
    with st.sidebar:
        st.markdown("## ℹ️ How to Use")
        st.markdown("""
        1. **Select a mode** - Choose what you want to do
        2. **Choose a model** - Pick your preferred AI model
        3. **Input your code/prompt** - Provide the content to work with
        4. **Submit** - Get AI assistance!
        """)
        
        st.markdown("---")
        
        st.markdown("## 🚀 Features")
        st.markdown("""
        - **Error Fixing**: Debug and fix code issues
        - **Code Improvement**: Enhance code quality
        - **Code Generation**: Create new code from requirements
        """)
        
        st.markdown("---")
        
        st.markdown("## API Setup")
        st.markdown("""
        Make sure to set your Groq API key:
        - **Recommended**: Edit `config.py` file
        - As `GROQ_API_KEY` environment variable
        - Or in Streamlit secrets
        """)
        
        if st.button("Get New API Key", key="get_api_key"):
            st.info("""
            **Getting a New API Key:**
            1. Visit [console.groq.com](https://console.groq.com)
            2. Sign in or create account
            3. Go to API Keys section
            4. Create new key and copy it
            5. Update your configuration
            
            **API Key Format:** `gsk_xxxxx...` (40+ chars)
            """)
        
        st.markdown("---")
        
        st.markdown("## Troubleshooting")
        st.markdown("""
        **Common Issues:**
        - **Organization Restricted**: Get new API key and update `config.py`
        - **Authentication Failed**: Check key format in `config.py`
        - **Invalid Request**: Verify key is active and correctly formatted
        
        **Priority Order:**
        1. `config.py` (recommended)
        2. Environment variable
        3. Streamlit secrets
        
        See `api_key_guide.md` for detailed help.
        """)


def clear_session_data():
    """Clear relevant session data."""
    keys_to_clear = ['code_input', 'additional_context']
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
