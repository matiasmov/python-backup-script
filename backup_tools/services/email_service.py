import sys
from datetime import date
import smtplib
from email.message import EmailMessage
from backup_tools.config_manager import PASSWORD, SENDER, PATH, RECEIVER

def email_report(filename, dataCode):
  
    today = date.today().strftime("%Y-%m-%d")
    
    msg = EmailMessage()
    msg['Subject'] = 'Relatório - SnipeIT - Backup'
    msg['From'] = {SENDER}
    msg['To'] = {RECEIVER}

    text = f"""Olá,

O processo de backup automático foi executado.

Status: {dataCode}
Arquivo: {filename}
Arquivo salvo em: {PATH}
Hora: {today}"""
    
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  
        smtp.login(SENDER, PASSWORD)
        smtp.send_message(msg)

    print("Sucess!.")