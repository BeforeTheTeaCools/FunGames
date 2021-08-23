from imap_tools import MailBox
from Account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
#alternative way to this so we dont have to logout at the end

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=2, reverse=True): #just .fetch() brings all the mails
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #bring unread messages
    # for msg in mailbox.fetch('(UNSEEN)'): 
        # print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(FROM beforetheteacools@gmail.com)', limit=1, reverse=True):#get mail from certain person 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(TEXT "test mail")'): #has certain word in mail in both title and body
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test mail")'): #has certain word in mail only in subject
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 15-Nov-2020)', reverse=True, limit=3): #mail after certain date
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(ON 15-Nov-2020)', reverse=True, limit=3): #mail on certain date
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #if i want 2 or more conditions
    for msg in mailbox.fetch('(SENTSINCE 15-Nov-2020 SUBJECT "Test mail")', reverse=True, limit=3): #mail after certain date
        print("[{}] {}".format(msg.from_, msg.subject))

    # #if it fills one of the 2 conditions
    # for msg in mailbox.fetch('(OR SENTSINCE 15-Nov-2020 SUBJECT "Test mail")', reverse=True, limit=3): #mail after certain date
    #     print("[{}] {}".format(msg.from_, msg.subject))

    #for these parts can look at pypi.org/project/imap-tools/ for more info