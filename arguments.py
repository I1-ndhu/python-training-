def add(mark1,mark2,mark3):
     return mark1+mark2+mark3

n=int(input("how many students?"))
students={}
for i in range(3):
    name=input(f"enter name of students {i+1}:")
    mark1 = int (input(f"enter the tamil mark of {name}:"))
    mark2 = int (input(f"enter the english mark of {name}:"))
    mark3 = int (input(f"enter the maths mark of {name}:"))
    a=add(mark1,mark2,mark3)
    students[name]=a
    print(f"mark of students{name}:",a)
topper=max(students,key=students.get)
print("topper:",topper,"with",students[topper],"marks")