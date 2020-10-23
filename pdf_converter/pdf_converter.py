# Python program to create a pdf file 

from fpdf import FPDF 

# Creating instance of the class 
pdf = FPDF() 

# Add a page 
pdf.add_page() 

# Set style and size of font  that you want in the pdf 
pdf.set_font("Arial", size = 15)

print("*"*25)
text1=input("Enter Title of the PDF : \n")


# Create a cell 
pdf.cell(200, 10, txt = text1, ln = 1, align = 'C')

print("*"*25)
text2=input("Enter Content of the PDF : \n")


# Add another cell 
pdf.cell(200, 10, txt = text2, ln = 2, align = 'C') 

print("*"*25)
namePdf=input("Enter name of the PDF : \n")

pdf.output(namePdf) 
