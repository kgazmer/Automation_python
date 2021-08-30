# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:27:09 2021

@author: ASUS
"""
#! /usr/bin/env python3
import os
import requests

dir_path="./supplier-data/descriptions/"
lst_file=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
lst_feedback=[]
dict_feedback={}
count=0
url="http://34.122.14.0/fruits/"
for file in lst_file:
  count=0
  with open(os.path.join(dir_path,file)) as f:        
    for line in f.readlines():
      if count==0:
        dict_feedback["name"]=line.strip('\n')
      elif count==1:
        dict_feedback["weight"]=line.strip('\n')
      elif count==2:
        dict_feedback["description"]=line.strip('\n')
      elif count==3:
        dict_feedback["image_name"]=line.strip('\n')
        lst_feedback.append(dict_feedback)
      else:
        dict_feedback={}
      count+=1

for i in range(len(lst_feedback)):
    p=lst_feedback[i]
    print(p)
    response = requests.post(url, data=p)
    print(response.status_code)


#%%
#! /usr/bin/env python3
import os
import requests

dir_path="./supplier-data/descriptions/"
lst_file=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
lst_feedback=[]
dict_feedback={}
count=0
url="http://34.67.47.175/fruits/"

for file in lst_file:
  count=0
  with open(os.path.join(dir_path,file)) as f:
    print(file," count=",count)
    for line in f.readlines():
      if count==0:
        dict_feedback["name"]=line.strip('\n')
      elif count==1:
        dict_feedback["weight"]=int(line[:-4])
      elif count==2:
        dict_feedback["description"]=line.strip('\n')
        dict_feedback["image_name"]=file[:-3]+"jpeg"
        lst_feedback.append(dict_feedback)
        print(lst_feedback)
        dict_feedback={}
      count+=1
for i in range(len(lst_feedback)):
    p=lst_feedback[i]
    print(p)
    response = requests.post(url, json=p)
    print(response.status_code)


    