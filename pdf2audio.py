"""
Project_Name: pdf file to audio converter
Descrition: This file will convert pdf file in audio
Credit: Inventive Arya
Instagram: Inventivearya
Gmail : inventivearya@gmail.com
"""

#Program 

import pyttsx3
import PyPDF2
book_name=input("Enter File Name: ")
page_num=int(input("Enter Page Number From Where You Want to Start: "))
book = open(book_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(page_num, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
