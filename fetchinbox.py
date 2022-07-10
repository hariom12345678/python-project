
# import required libraries
import imaplib
#import send
import email
from email.header import decode_header
import webbrowser
import os
import datetime 
import sent 

# use your email id here
username = "itnoc1@powergrid.co.in"
  
# use your App Password you
# generated above here.
password ="Adm!n1Noc"
  
# creata a imap object
imap = imaplib.IMAP4_SSL("imap.mail.gov.in")
  
# login
result = imap.login(username, password)
  
# Use "[Gmail]/Sent Mails" for fetching
# mails from Sent Mails. 
imap.select('test', 
readonly = True) 
  
response, messages = imap.search(None, '(FROM "hariommishra01236@gmail.com")')
messages = messages[0].split()
  
# take it from last
latest = int(messages[-1])
  
# take it from start
oldest = int(messages[0])
  
for i in range(latest, latest-1, -1):
    # fetch
    res, msg = imap.fetch(str(i), "(RFC822)")
      
    for response in msg:
        if isinstance(response, tuple):
  
           msg = email.message_from_bytes(response[1])
           # print required information
           print(msg["Date"])
           datestring=msg["Date"]
           d = datetime.datetime.strptime(datestring, "%a, %d %b %Y %H:%M:%S %z")
           t1=d.strftime("%Y-%m-%d-%H:%M:%S")
           print(t1)
           d1 = datetime.datetime.strptime(t1, "%Y-%m-%d-%H:%M:%S")
           print("recieved time",d1)
           print(msg["From"])
           print(msg["Subject"])
           t3=sent.msg["Date"]
           print("sent time",t3)
           d = datetime.datetime.strptime(t3, "%a, %d %b %Y %H:%M:%S %z")
           t4=d.strftime("%Y-%m-%d-%H:%M:%S")
           d2 = datetime.datetime.strptime(t4, "%Y-%m-%d-%H:%M:%S")
           print("sent time",d2)
           print("time invertal ",d2-d1)
  #===========================================
    for part in msg.walk():
        if part.get_content_type() == "text / plain":
            # get text or plain data
            body = part.get_payload(decode = True)
            print(f'Body: {body.decode("UTF-8")}', )