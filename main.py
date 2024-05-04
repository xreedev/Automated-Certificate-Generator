import extractExcel as EX
import updateWord as UW
import os
from docx2pdf import convert
student_files=os.listdir("student_data")
for file in student_files:
 student_list=EX.extractData(f"student_data\\{file}")
 UW.addInfo(student_list,"template.docx")

file_list=os.listdir("Final_Word")
for file in file_list:
  convert(f"Final_Word\\{file}",output_path="Final_Certificates\\Sports")



