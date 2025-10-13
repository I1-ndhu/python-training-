n=int(input("how many students?"))
students={}
for i in range(3):
    name=input("enter name of students (i+1):")
    mark1 = int (input("enter the tamil mark of (name):"))
    mark2 = int (input("enter the english mark of (name):"))
    mark3 = int (input("enter the maths mark of (name):"))
    studentmark=mark1+mark2+mark3
    students[name] = studentmark
    topper=max(students,key=students.get)
    print("topper:")

