class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    #def method(self):
       # print(self.name,self.marks)
#stu1=Student("ramesh",96)
#stu2=Student("suresh",90)
#stu1.method()
#stu2.method()
#another type of using method concept
    def getdetails(self):
        print(f"{self.name} and his marks is {self.marks}")
    def getdetails1(self):
        print(f"{self.name} and his marks is {self.marks}")   
stu1=Student("ramesh",96)
stu2=Student("suresh",90)
stu1.getdetails()
stu2.getdetails1() 