# Automation_python
Final graded assessment of Google Python

In this assessment by Google/Coursera you are required to firstly change image dimensions using PIL library after downloading/extracting images provided to a directory. 
The code in the second part of changeImage.py (after #%%- ) accomplishes this. 
For the upload part again the second part of the supplier_image_upload.py needs to be used as the first part uploads all images and files in 'usr/share/apache2/icons/' which is not required.
Again 2nd part of run.py posts the details of item using json to the url that is provided by the qwiklabs. 
reports.py generates report in the format as specified by the client(here examiner)
emails.py contains two functions that generates and sends email.
report_email.py generates report in the format specified using "generate_function" in reports.py and then generates/sends email using emails.py.
Finally health_check.py checks health of cpu/ram/diskspace using psutil/shutil and hostname resultion of localhost using socket libs every 60 seconds and sends email if any of these functions returns false meaning some issue.

These codes are not refined and are in the form that was presented to the examiner. 
All server details and student id wherever used need to be changed as provided by qwiklabs.
