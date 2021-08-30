# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:08:39 2021

@author: ASUS
"""
#!/usr/bin/env python3

import os
import reports
import emails
import datetime

dir_path="./supplier-data/descriptions/"
#dir_path="C:/Users/ASUS/Documents/PythonExercises/Google/6/2/files/"
def get_data():
  lst_file=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
  lst_pdf_data="<br/>"
  for file in lst_file:
    count=0
    with open(os.path.join(dir_path,file)) as f:      
      for line in f.readlines():    
        if count==0:
          lst_pdf_data=lst_pdf_data + "name: " + line + "<br/>"
        elif count==1:
          lst_pdf_data=lst_pdf_data + "weight:" + line + "<br/>"
        elif count==2:
          lst_pdf_data=lst_pdf_data + "<br/>" 
        else:
          continue
        count+=1
  print(lst_pdf_data)
  return lst_pdf_data

def get_date():   
  today = datetime.date.today()
  return today.strftime("%B %d, %Y")

def main():
  data=get_data()
  
  date_now=get_date()
  #filename='C:/Users/ASUS/Documents/PythonExercises/Google/6/2/files/processed.pdf'
  filename='/tmp/processed.pdf'
  title= "Processed Update on "+date_now
  reports.generate_report(filename, title, data) 
  sender="automation@example.com"
  recipient="@example.com"
  subject="Upload Completed - Online Fruit Store"
  body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment=filename
  message=emails.generate_email(sender, recipient, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main()
