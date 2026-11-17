#---------OM NAMA SHIVAYA -----------JAI HIND --------JAI BHARATH MATA--------
total_students=int(input("Enter the total number of students:"))
my_students_list=[]
for i in range (1,total_students+1):
    print(f"Student {i}")
    name=input("Enter the name of the Student:")
    marks_python=float(input("Enter the marks of python:"))
    marks_mathematics=float(input("Enter the marks of mathematics:"))
    marks_english=float(input("Enter the marks of English:"))
    my_students_list.append({
        "name":name,
        "marks_python":marks_python,
        "marks_mathematics":marks_mathematics,
        "marks_english":marks_english
    })
print("============STUDENT REPORT CARD=================")
average_list=[]
for student in my_students_list:
        print("Name:",student["name"])
        print("Marks in Python:",student["marks_python"])
        print("Marks in Mathematics:",student["marks_mathematics"])
        print("Marks in English:",student["marks_english"])
        total_marks=student["marks_python"]+student["marks_mathematics"]+student["marks_english"]
        print("Total Marks:",total_marks)
        print("Average Marks:",total_marks/3)
        average_marks=total_marks/3
        average_list.append({
             student["name"]:average_marks
        })
        if average_marks>=90:
            print("Result:VERY EXCELLENT")
        elif average_marks>=75 and average_marks<90:
            print("Result:VERY GOOD")
        elif average_marks>=50 and average_marks<75:
            print("Result:GOOD")
        else:
            print("Result:NEEDS IMPROVEMNT")
        print("--------------------------------------------------------------")
        print()
        
#FINDING THE HIGHEST SCORIUNG STUDENT
my_list=[]
for student in my_students_list:
    total_marks=student["marks_python"]+student["marks_mathematics"]+student["marks_english"]
    my_list.append({
        "name":student["name"],
        "total_marks":total_marks
    })
if total_students!=0:
    Highest_score=max(my_list,key=lambda x:x["total_marks"])
    print("Highest scoring student is:",Highest_score["name"],"with total marks:",Highest_score["total_marks"])
else:
     print("No students are there in a college")
     

