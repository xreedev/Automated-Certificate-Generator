import extractExcel as EX
import updateWord as UW
import os
from docx2pdf import convert
student_files=os.listdir("student_data") #extract all csv files
for file in student_files:
 student_list=EX.extractData(f"student_data\\{file}") #extract data from csv file and store in list
 UW.addInfo(student_list,"template.docx") #add info to template

file_list=os.listdir("Final_Word")#take each docx final file
for file in file_list:
  convert(f"Final_Word\\{file}",output_path="Final_Certificates\\Sports") #convert to pdf



