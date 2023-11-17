from config.settings import hotel_email,password_email
from email.message import EmailMessage
import smtplib
import random
# -------------------------------------------------------------------------------------------------------------------------------
def send_mail(send_to,code):

    msg = EmailMessage()
    msg['Subject'] = 'کد اعتبار سنجی سایت هتل'
    msg['From'] = hotel_email
    msg['To'] = send_to
    msg.set_content(f"کد شما: {code}")

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(hotel_email,password_email)
        server.send_message(msg)
# -------------------------------------------------------------------------------------------------------------------------------
