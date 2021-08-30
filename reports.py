# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:42:16 2021

@author: ASUS
"""

#!/usr/bin/env python3
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
def generate_report(filename,title,data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])      
  report_paragraph = Paragraph(data)      
  report.build([report_title, report_paragraph])
  





