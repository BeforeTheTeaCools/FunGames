#pip install imap-tools
from imap_tools import MailBox
from Account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

for msg in mailbox.fetch(limit=1, reverse=True): #get only one mail and get recent ones first = reverse = True
    print("title:", msg.subject)
    print("sender:", msg.from_)
    print("recipient:", msg.to)
    print("date:", msg.date)
    print("body:", msg.text)
    print("HTML", msg.html)
    print("=" * 100)

    #attachments
    for att in msg.attachments:
        print("attachment name:", att.filename)
        print("type:", att.content_type)
        print("size:", att.size)
        #file download
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload) #write above attachment info into file
            print("attachment {} download complete".format(att.filename))

mailbox.logout()