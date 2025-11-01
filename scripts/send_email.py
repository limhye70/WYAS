import smtplib
import os
import pandas as pd
from constant import HOURS, GEO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

def top_trends_html():

    df = pd.read_csv('data/trends_table.csv', encoding='utf-8-sig')
    html_table = df.to_html(index=False).replace("arrow_upward", "&#x2191;").replace("arrow_downward", "&#x2193;")
    # import timestamp
    with open("data/timestamp.txt", "r", encoding='utf-8') as file:
        timestamp = file.read()

    # Create HTML body
    html = f"""
    <html>
    <body>
        <p>Good morning!,<br><br>

        I hope you had a restful night. Below is a summary of key U.S. economic topics trending on Google over the last 24 hours, sourced from Google Trends.
        </p>
        {timestamp}<br>
        {html_table}
        <p>Best regards,<br>WYAS</p>
        Notes:<br>
        <ul>
        <li>"Trending" indicates ongoing search interest; "Peaked" indicates the topic surged but has since declined.</li><br>
        <li>Data reflects U.S. market activity while you were sleeping in Singapore.</li>
        </ul>
    </body>
    </html>
    """

    return html


def send_email():
    # Load environment variables from .env file if present
    load_dotenv("./.env")

    sender_email = os.getenv("EMAIL_SENDER")
    reciever_email = os.getenv("EMAIL_RECEIVER")
    password = os.getenv("EMAIL_PASSWORD")
    subject = os.getenv("EMAIL_SUBJECT", "Morning Update: U.S. Economic Trends (Past 24 Hours)")
 

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = reciever_email
    message['Subject'] = subject

    html = top_trends_html()
    message.attach(MIMEText(html, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)
        print("Email sent successfully")

if __name__=="__main__":
    send_email()

