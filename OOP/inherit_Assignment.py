from __future__ import print_function
import datetime

class College:
    def __init__(self):
        self.collegeName = "Khwopa"
        self.location = "Bkt"

class Faculty(College):
    def __init__(self,fac):
        self.facultyName = fac
        College.__init__(self)

class Teacher(Faculty):
    def __init__(self,name,period,salary,fac):
        self.name = name
        self.period = period
        self.salary = salary
        Faculty.__init__(self,fac)

    def info(self):
        print("Name \t: ",self.name)
        print("Period \t: ",self.period)
        print("Salary \t: ",self.salary)
        print("Faculty\t: ",self.facultyName,"\n")

class Student(Faculty):
    def __init__(self,name,sub,mark,fac):
        self.name = name
        self.subject = sub
        self.mark = mark
        Faculty.__init__(self,fac)

    def result(self):
        if self.mark >= 90:
            print("Excellent!")
        elif self.mark >= 80:
            print("Good!")
        elif self.mark >= 60:
            print("Satisfactory!")
        else:
            print("Not Good")

    def info(self):
        print("Name \t: ",self.name)
        print("Subject\t: ",self.subject)
        print("Marks \t: ",self.mark)
        print("College\t: ",self.collegeName)

teach1 = Teacher("Roshan",4,30000,"Computer")
teach1.info()

stud1 = Student("Kiran","Physics",55,"Computer")
stud1.info()
print("Remarks\t: ",end=" ")
stud1.result()

print(datetime.datetime.now())
x = datetime.datetime.now()