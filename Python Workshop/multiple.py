student1="Punith D U"
student2="Jashwanth D B"
student3="Sagar"
student4="Akhilesh A G"
student5="Azam Z"


statement='Python'
statement1="let's go to Lunch"


 


student_names=["Punith D U","Jashwanth D B","Sagar","Akhilesh A G","Azam Z","Akash H",
              "Karthik T S","Adarsh","Dhanush D","Darshan G","Abhishek G M"];
print(student_names)
print("------------------")
print(student_names[1])
print("------------------")
print(student_names[-1])
print("------------------")
student_names[1]="Babu"
print(student_names)
print("--------------")
student_names.append("baba")
print(f"added baba:{student_names}")
print("------------------------------")
student_names.remove("Akash H")
print(f"remove Akash H:{student_names}")
print("-----------------")
student_names.insert(1,"Om")
print(student_names)
print("-------------------")
student_names.pop(3)
print(f"Length of list:{len(student_names)}")
print(student_names.reverse())
