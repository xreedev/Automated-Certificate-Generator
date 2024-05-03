import csv
from Student import Student

def extractData(filename):
    # Open the CSV file
    final_list=[]
    with open(filename, newline='') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
         # print(row)
         if(len(row)==7):
            student=Student(row[1],row[3],row[4],row[5],row[6])
         elif(len(row)==6):
            student = Student(row[1], row[3], row[4], row[5], "")
         elif (len(row) == 4):
             student = Student(row[0], row[1], row[2], row[3], "")
         final_list.append(student)
    return final_list

# l=extractData("student_data//girlsfull.csv")
# for i in l:
#     print(i.name,i.event2)