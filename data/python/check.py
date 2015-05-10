# pyMailCheck.py - Logs into your gmail and prints the number of unread emails.
# Place this file in the top level of your Galileo's SD card.

import imaplib  # Used to connect to an IMAP4 server.
obj = imaplib.IMAP4('imap.gmail.com', '80')  # Connect to an IMAP4 sever over SSL, port 993
obj.login('anirudhqazxswced@gmail.com','numbercrosshard')  # Identify the client user and password
obj.select()  # Select a the 'INBOX' mailbox (default parameter)
# Search mailbox no (None) charset, criterion:"UnSeen". Will return a tuple, grab the second part,
# split each string into a list, and return the length of that list:
print len(obj.search(None,'UnSeen')[1][0].split())
