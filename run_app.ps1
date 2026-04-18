# PowerShell script to activate virtual environment and run the Streamlit app
Write-Host "Activating virtual environment..." -ForegroundColor Green
.\venv\Scripts\activate

Write-Host "Starting AI Code Assistant..." -ForegroundColor Green
streamlit run main.py

# Keep the window open
Read-Host "Press Enter to exit"
