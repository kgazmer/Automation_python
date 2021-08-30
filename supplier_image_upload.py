# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:17:37 2021

@author: ASUS
"""
#! /usr/bin/env python3
import requests
import os
dir_path='usr/share/apache2/icons/'
url="http://localhost/upload/"
lis_files=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
if '.DS_Store' in lis_files:
  lis_files.pop(lis_files.index('.DS_Store'))
for file in lis_files:
  with open(os.path.join(dir_path,file),'rb') as opened:
    r=requests.post(url,file={'file':opened})      
    print(r.status_code)
    
#%%
#! /usr/bin/env python3
import requests
import os
dir_path='./supplier-data/images'
url="http://localhost/upload/"
lis_files=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
if '.DS_Store' in lis_files:
  lis_files.pop(lis_files.index('.DS_Store'))
for file in lis_files:
  with open(os.path.join(dir_path,file),'rb') as opened:
    r=requests.post(url,files={'file':opened})
    print(r.status_code)

    