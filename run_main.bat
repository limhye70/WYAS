@echo off
REM Batch file to run the main script
REM 
REM Instructions:
REM 1. If Python is not in your PATH, replace 'python' below with your full Python path
REM    Example: "C:\Users\YourName\AppData\Local\Programs\Python\Python313\python.exe"
REM 2. Ensure you have created a .env file with your email credentials (see env.example)
REM 3. Install required packages: pip install -r requirements.txt
python scripts\main.py
pause