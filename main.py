"""
Main Streamlit application for AI Code Assistant.
Provides interface for error fixing, code improvement, and code generation using Groq API.
"""

import streamlit as st
import sys
import os

# Add modules directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from groq_client import initialize_groq_client
from ui_helpers import (
    setup_page_config,
    render_header,
    render_mode_selection,
    render_model_selection,
    render_code_input_area,
    render_quick_suggestions,
    render_submit_button,
    render_response_area,
    render_sidebar_info,
    clear_session_data
)


def main():
    """Main application function."""
    # Setup page configuration
    setup_page_config()
    
    # Initialize session state variables
    if 'mode' not in st.session_state:
        st.session_state.mode = None
    if 'response_data' not in st.session_state:
        st.session_state.response_data = None
    if 'selected_model' not in st.session_state:
        st.session_state.selected_model = None
    
    # Render sidebar
    render_sidebar_info()
    
    # Render main header
    render_header()
    
    try:
        # Initialize Groq client
        groq_client = initialize_groq_client()
        available_models = groq_client.get_available_models()
        
        # Main content area with two columns
        col_left, col_right = st.columns([1, 1])
        
        with col_left:
            # Mode selection
            selected_mode = render_mode_selection()
            
            if selected_mode:
                # Model selection
                selected_model = render_model_selection(available_models)
                
                # Only proceed if model selection was successful
                if selected_model:
                    # Code input area
                    code_input, additional_context = render_code_input_area(selected_mode)
                    
                    # Submit button
                    submitted = render_submit_button()
                    
                    # Handle form submission
                    if submitted and code_input.strip():
                        with st.spinner("AI is thinking..."):
                            response_data = groq_client.get_response(
                                mode=selected_mode,
                                code=code_input,
                                model_name=selected_model,
                                additional_context=additional_context
                            )
                            st.session_state.response_data = response_data
        
        with col_right:
            # Right side panel
            if st.session_state.mode:
                # Quick suggestions
                selected_suggestion = render_quick_suggestions(st.session_state.mode)
                
                # Update code input if suggestion is selected
                if selected_suggestion:
                    if st.session_state.mode == "Fix Error":
                        suggestion_text = f"I'm getting a {selected_suggestion.lower()} in my code. Please help me fix it."
                    elif st.session_state.mode == "Improve Code":
                        suggestion_text = f"Please improve my code focusing on {selected_suggestion.lower()}."
                    else:  # Generate Code
                        suggestion_text = f"Generate a {selected_suggestion.lower()} for me."
                    
                    # Update the code input in session state
                    if 'code_input' in st.session_state:
                        st.session_state.code_input = suggestion_text
                        st.rerun()
                
                # Display response area
                if st.session_state.response_data:
                    render_response_area(st.session_state.response_data)
                
                # Clear button
                if st.button("🗑️ Clear All", key="clear_all", use_container_width=True):
                    clear_session_data()
                    st.session_state.response_data = None
                    st.rerun()
            else:
                st.info("👈 Please select a mode to get started!")
    
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.markdown("""
        ### Setup Required:
        1. Get your Groq API key from [groq.com](https://groq.com)
        2. Add it to `config.py` file (recommended)
        3. Or set it as environment variable: `GROQ_API_KEY=your_key_here`
        4. Or add it to your Streamlit secrets
        
        **Config File Setup (Recommended):**
        Edit `config.py`:
        ```python
        GROQ_API_KEY = "your_api_key_here"
        ```
        
        **Environment Variable Setup:**
        ```bash
        export GROQ_API_KEY="your_api_key_here"
        ```
        
        **Streamlit Secrets Setup:**
        Create `.streamlit/secrets.toml`:
        ```toml
        GROQ_API_KEY = "your_api_key_here"
        ```
        """)
    
    except Exception as e:
        st.error(f"❌ Unexpected Error: {str(e)}")
        st.markdown("Please check your configuration and try again.")


if __name__ == "__main__":
    main()
