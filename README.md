# WYAS (While You Are Sleeping) — Global Economy Trends Morning Update

## Overview
**WYAS** is an automated tool that delivers daily morning updates on global economic trends by:
- Collecting top trending keywords from Google Trends
- Generating a formatted HTML summary
- Delivering insights via email at your preferred time

---

## Project Structure
```
wyas/
├── run_main.bat          # Batch file for Windows Task Scheduler
├── scripts/
│   ├── main.py           # Pipeline orchestrator
│   ├── read_trends.py    # Data collection logic
│   ├── send_email.py     # Email formatting and delivery
│   └── constant.py       # Configuration settings
├── data/                 # Runtime data storage
├── .env                  # Environment variables
└── requirements.txt      # Dependencies
```

## Setup Instructions

### 1. Environment Configuration
Create a `.env` file in the project root with your email settings:
```env
EMAIL_SENDER=your_email@gmail.com # gmail only
EMAIL_PASSWORD=your_app_password_here
EMAIL_RECEIVER=recipient_email_1@gmail.com, recipient_email_2@outlook.com
EMAIL_SUBJECT=Morning Update: U.S. Economic Trends (Past 24 Hours)
```

### 2. Update Batch File Path
Edit `run_main.bat` with your project directory:
```batch
cd C:\path\to\your\WYAS\directory
```

### 3. Schedule Daily Updates (Windows)
1. Open Task Scheduler
2. Click "Create Basic Task"
3. Set your preferred schedule (e.g., daily at 7 AM)
4. Point to your `run_main.bat` file

## Requirements
- Python 3.9+
- Required packages listed in `requirements.txt`

## Usage
Once configured, WYAS will automatically:
- Run at your scheduled time
- Collect latest economic trends
- Send formatted updates to specified email(s)

Note: Ensure your computer is powered on at the scheduled time for the task to execute.
