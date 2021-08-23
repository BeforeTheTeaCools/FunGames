import smtplib
from Account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo() #check for connection
    smtp.starttls() #everything is encrypted
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "test mail" #mail title
    body = "mail body" #body


    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, "beforetheteacools@gmail.com", msg) #sender,receiver,msg

