import PyPDF2
import os

pdffileobj = open('core_rules_update_9th.pdf', 'rb')

pdfreader=PyPDF2.PdfFileReader(pdffileobj)

x=pdfreader.numPages
pageobj=pdfreader.getPage(x+1)

text=pageobj.extractText()

file1=(r"D:\Assets\warhammer_40000\hdlFJHJZCEwPWjwf.txt", "a")
file1.writelines(text)