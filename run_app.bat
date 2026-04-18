@echo off
echo Activating virtual environment...
call venv\Scripts\activate

echo Starting AI Code Assistant...
streamlit run main.py

pause
