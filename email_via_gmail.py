#!/usr/bin/python3
# -*- coding: utf-8 -*-
import smtplib
from datetime import datetime
from GMAIL_PWD import GMAIL_PWD

str_ing = open('mailText.txt', 'r').read()

# with open('mailText.txt', 'r') as myfile:
#     data = myfile.read()


subject = 'Daily Exchange {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M"))
fromMessage = 'marius.tao@gmail.com'
toMessage = 'marius.a.nicolae@outlook.com'
text = str_ing

BODY = '\r\n'.join(['To: %s' % toMessage,
                    'From: %s' % fromMessage,
                    'Subject: %s' % subject,
                    '', text])

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('marius.tao@gmail.com', GMAIL_PWD)

try:
    server.sendmail(fromMessage, [toMessage], BODY)
    print('email sent')
except:
    print('error sending mail')

server.quit()

