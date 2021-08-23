import smtplib
from Account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Test mail"
msg["From"] = EMAIL_ADDRESS
msg["To"] = "beforetheteacools@gmail.com"
msg.set_content("please download the file")

#msg.add_attachment()
with open("rm6sqwpmesb41.jpeg", "rb") as f:
    #go to MIME type to look for what to type
    msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)