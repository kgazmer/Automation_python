# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:50:14 2021

@author: ASUS
"""
import psutil
import shutil
import socket
import time
import emails
def check_cpu_usage():
  percent=80
  usage = psutil.cpu_percent(1)  
  return usage <= percent

def check_disk_usage():
  du = shutil.disk_usage("C:")
  percent_free = 100 * du.free / du.total
  return percent_free >= 20

def check_memory():
  mem_used=psutil.virtual_memory()[4]  
  return (mem_used/2**20) >= 500


def hostname_resolves():
  try:
    hostname ="localhost"
    if socket.gethostbyname(hostname)=="127.0.0.1":
      return True
  except socket.error:
    return False
#check_disk_usage()  
#check_memory()
print(hostname_resolves())
sender ="automation@example.com"
recipient="@example.com"
body="Please check your system and resolve the issue as soon as possible."
def main():  
  subject=""
  while True:
    if not check_cpu_usage():
      subject="Error - CPU usage is over 80%"
    elif not check_disk_usage():
      subject="Error - Available disk space is less than 20%" 
    elif not check_memory():
      subject="Error - Available memory is less than 500MB"  
    elif not hostname_resolves():
      subject="Error - localhost cannot be resolved to 127.0.0.1"  
    if subject !="":  
      message= emails.generate_email(sender,recipient,subject,body,"") 
      emails.send_email(message)
    time.sleep(60)
if __name__ == "__main__":
  main()