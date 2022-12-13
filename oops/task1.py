class Employee: #creating a class
    company ="Aditya Engineering College"  #class Attribute
    def __init__(self,name,age,salary): #default constructor
        #name age salary are attributes
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):# creating method to print output
        print(self.name,self.age,self.salary)
emp1=Employee("mani",25,35000) #creating objects
emp2=Employee("hani",30,40000)
emp1.display()
emp2.display()
print(f"{emp1.name} and {emp2.name} works in {emp1.__class__.company}") #writing or creating formating string
print(f"{emp1.name}'s {emp1.age} and his salary is {emp1.salary}")
print(f"{emp2.name}'s {emp2.age} and his salary is {emp2.salary}")
