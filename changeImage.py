# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:02:58 2021

@author: ASUS
"""
#! /usr/bin/env python3
import os
from PIL import Image
dir_path='./images/'
dest_path= '/opt/icons/'
lis_files=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
#subprocess.call(["mv",dir_path+lis_files[1],dir_path+lis_files[1] + ".jpeg"])
if '.DS_Store' in lis_files:
  lis_files.pop(lis_files.index('.DS_Store'))


for file in lis_files:
  image_file=dir_path+file
  #subprocess.call(["mv",dir_path+lis_files[1], image_file])
  filename=[]
  im = Image.open(image_file)
  im_m = im.convert("RGB")
  im_m = im_m.resize((600,400))
  im_m.save(dest_path +file, "JPEG")

#%%
#! /usr/bin/env python3
import os
from PIL import Image
dir_path='./supplier-data/images/'
dest_path= './supplier-data/images/'
lis_files=[f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
#subprocess.call(["mv",dir_path+lis_files[1],dir_path+lis_files[1] + ".jpeg"])
if '.DS_Store' in lis_files:
  lis_files.pop(lis_files.index('.DS_Store'))
if 'LICENSE' in lis_files:
  lis_files.pop(lis_files.index('LICENSE'))
if 'README' in lis_files:
  lis_files.pop(lis_files.index('README'))



for file in lis_files:
  image_file=dir_path+file
  filename=file[:-5]+".jpeg"
  #subprocess.call(["mv",dir_path+lis_files[1], image_file])
  print(image_file)
  im = Image.open(image_file)
  im_m = im.convert("RGB")
  im_m = im_m.resize((600,400))
  im_m.save(dest_path + filename, "JPEG")
