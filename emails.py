# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:42:29 2021

@author: ASUS
"""

from email.message import EmailMessage
import mimetypes
import os.path
import smtplib

def generate_email(sender,recipient,subject,body,attachment):
  message = EmailMessage()
  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = subject
  message.set_content(body)
  if attachment!= "":
    attachment_path = attachment
    attachment_filename = os.path.basename(attachment_path)  
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as ap:
      message.add_attachment(ap.read(),
                             maintype=mime_type,
                             subtype=mime_subtype,
                             filename=attachment_filename)
  
  return message

def send_email(message):
  mail_server = smtplib.SMTP('localhost')  
  #sender=""
  #password=""
  #mail_server.login(sender, password)
  mail_server.send_message(message)