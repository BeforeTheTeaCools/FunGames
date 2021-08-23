import smtplib
from Account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Test mail"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "beforetheteacools@gmail.com"
#for multiple ppl do msg["To"] = "beforetheteacools@gmail.com, beforetheteacools@gmail.com" and etc

#if i want to do list then i can do
#to_list = ["beforetheteacools@gmail.com", "beforetheteacools@gmail.com"]
#msg["To"] = ", ".join(to_list)

#for CC do msg["Cc"] = "beforetheteacools@gmail.com"
#Bcc

msg.set_content("test")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)