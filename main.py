import extractExcel as EX
import updateWord as UW
import os
from docx2pdf import convert
# student_files=os.listdir("student_data")
# student_files=["cricket.csv","volleyball.csv","basketball.csv"]
# for file in student_files:
#  student_list=EX.extractData(f"student_data\\{file}")
#  UW.addInfo(student_list,"template.docx")

#convert("C:\\Users\\dell\\PycharmProjects\\pythonProject8\\Final_Word\\Adita. P. Nair_certificate.docx")

file_list=os.listdir("Final_Word2")
for file in file_list:
    convert(f"Final_Word//{file}",output_path="Final_Certificates")



