

class HS:
    x=5
    y=10.5
p1=HS()
print(p1.x)
print(HS.y)

class student:
    rno=123
    name="abc"
    branch="cse"
    def read(self):
        print("read")
    def write(self):
        print("write")
s1=student()
s1.read()
s1.write()
print(s1.name)
print(s1.rno)
print(s1.branch)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
        print("My age is :",self.age)
p1=Person("Jhon",36)
p2=Person("Faisal",18)
p1.myfunc()
p2.myfunc()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is "+self.name)
        print("My age is :",self.age)
p1=Person("Jhon",36)
p2=Person("Faisal",18)
p1.myfunc()
p2.myfunc()

class data:
    def __init__(self,x):
        print("In class method....")
        self.x=x
        print("The value is : ",x)
p1=data(5)
p1.__init__(30)

class Student:
    school_name='LVS'
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Harry",12)
print('Student:',s1.name,s1.age)
print('school name:',Student.school_name)

class Student:
    school_name='LVS'
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Harry",12)
print('Student:',s1.name,s1.age)
print('School name:',Student.school_name)
s1.name='Jessa'
s1.age=14
print('Student:',s1.name,s1.age)
Student.school_name='UMWS'
print('School name:',Student.school_name)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=18
        print("init")
        print(self.name)
        print(self.age)
p1=Person("Faisal",18)
p1.age=40
print(p1.age)

class Student:
    def __init__(self,n,a,m):
        self.name=n
        self.age=a
        self.marks=m
    def display(self):
        print("Name is",self.name)
        print("Age is",self.age)
        print("Marks is",self.marks)
s2=Student("Faisal",18,90)
s2.display()

class Student:
    def __init__(self,n,a,*m):
        self.name=n
        self.age=a
        self.marks=m
    def display(self):
        print("Name is",self.name)
        print("Age is",self.age)
        print("Marks is",self.marks)
s2=Student("Faisal",18,15,14,20)
s2.display()

class Student:
    def __init__(self,n,a,**m):
        self.name=n
        self.age=a
        self.marks=m
    def display(self):
        print("Name is",self.name)
        print("Age is",self.age)
        print("Marks is",self.marks)
s2=Student("Faisal",18,eng=15,maths=18,phy=20)
s2.display()

class Student:
    def __int__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def calculate_age(cls,name,birth_year):
        return cls(name,date.today().year-birth_year)
    def show(self):
        print(self.name,"s age is: ", str(self.age))
faisal=Student('Faisal', 18)
faisal.show()
joy=Student.calculate_age("Joy",1995)
joy.show()

class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)
Employee.sample(10)
emp=Employee()
emp.sample(2)

class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)
Employee.sample(10)
emp=Employee()
emp.sample(20)

class HS:
    def pdisplay(self):
        print("Inside the HS class")
class kk(HS):
    def odisplay(self):
        print("Inside child class")
p1=kk()
p1.odisplay()
p1.pdisplay()

class G1:
    def cdisplay(self):
        print("Inside the child class")

class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
class Car(Vehicle):
    def Car_info(self):
        print('Inside car class')
car=Car()
car.Vehicle_info()
car.Car_info()

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x=Student("Mike","Olsen")
x.printname()

class Vehicle:
    def info(self):
        print("This is a vehicle")
class Car(Vehicle):
    def car_info(self, name):print("Truck name is:", name)
class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

obj1=Car()
obj1.info()
obj1.car_info('BMW')

obj2=Truck()
obj2.info()
obj2.truck_info('Ford')

class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle")
class Car(Vehicle):
    def car_info(self, name):print("Truck name is:", name)
class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)
class Sportscar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside sportscar class")

s_car=Sportscar()
s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()

class Animal:
    def walk(self):
        print('Hello, I am the parent class')
class Dog(Animal):
    def walk(self):
        print('Hello, i am the child class')
print('The method walk here is overhidden in the code')

r=Dog()
r.walk()

r=Animal()
r.walk()

class CounterClass:
    __privateCount=0
    def count(self):
        self.__privateCount+=1
        print(self.__privateCount)
counter=CounterClass()
counter.count()
counter.count()
counter.count()
print(counter.__privateCount)

class Speed:
    def __init__(self):
        self.speed=10
        self.__newspeed=20
        self.distance=40
    def disp(self):
        print("Speed is:",self.speed)
        print("New speed is:",self.__newspeed)
s1=Speed()
# s1.disp()
print(s1.speed)
print(s1.distance)
print(s1.__newspeed)

class Speed:
    def __init__(self):
        self.speed=10
        self.__newspeed=20
        self.distance=40
    def disp(self):
        print("Speed is:",self.speed)
        print("New speed is:",self.__newspeed)
        print("Distance is",self.distance)
s1=Speed()
s1.disp()
print(s1.speed)
print(s1.distance)
s1.__newspeed=70
print(s1.__newspeed)

class Speed:
    def __init__(self):
        self.speed=10
        self.__newspeed=20
        self.distance=40
    def get_new_speed(self):
        return self.__newspeed
    def disp(self):
        print("Speed is:",self.speed)
        print("New speed is:",self.__newspeed)
        print("Distance is",self.distance)
s1=Speed()
s1.disp()
print(s1.speed)
print(s1.distance)
print(s1.get_new_speed)

def area(l, b):
     c=l*b
     return c
def area(size):
    c=size*size
    return c
print(area(4))

class Compute:
    def area(self, x=None, y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
obj=Compute()
print(obj.area(2,8))

oldfile="file.txt"
Newfile="new.txt"
def copyFile(oldFile, newFile):
    f1=open(oldFile, "r")
    f2=open(newFile, "w")
    while True:
        text=f1.read(50)
        if text=="":
            break
        f2.write(text)
    f1.close()
    f2.close()

f=open("D:/pythonproject/newfile.txt","w")
f.write("This is the file in new Directory")

f=open("C:/pythondummy/newfile.txt","w")
f.write("This is the file in new Directory")
import os
os.remove("C:/pythondummy/newfile.txt")

import os
os.rmdir("C:/pythondummy/newfile.txt")

import pickle
f=open("test.pck","wb")
# pickle.dump(12.3,f)
# f.close()
pickle.dump({1,2,3},f)
f.close()

f=open("test.pck","rb")
x=(pickle.load(f))
print(x)
print(type(x))
f.close()

a=int(input("Enter the n1"))
b=int(input("Enter the n2"))
try:
    c=a*b
    print("Answer is",c)
except:
    print("zero error")

a=int(input("Enter the n1"))
b=int(input("Enter the n2"))
try:
    c=a*b
    print("Answer is",c)
except ZeroDivisionError:
    print("zero error present in",b)

def number():
    x=input()
    if(x=='17'):
        raise ValueError("Not good")
number()

import re
str="HELLO PYTHON PROGRAMMING"
x=re.findall("L",str)
print(x)

import re
str="HELLO PYTHON PROGRAMMING"
x=re.search("P",str)
print(x.string)

import re
str="HELLO PYTHON PROGRAMMING"
x=re.split("PYTHON",str)
print(x)

import re
str="HELLO PYTHON PROGRAMMING"
x=re.split(" ",str,2)
print(x)

import re
str="HELLO PYTHON PROGRAMMING"
x=re.sub("P","G",str)
print(x)

import re
str="HELLO PYTHON PROGRAMMING"
x=re.findall("[P]",str)
print(x)

import re
str="Example for Meta Characters in Regular Expression"
x=re.findall("^Meta",str)
print(x)

import re
str="Example for Meta Characters in Regular Expression"
x=re.findall("Expression$",str)
print(x)


import re
str="Example for Meta Characters in Regular Expression"
x=re.findall("Exam........",str)
print(x)


import re
str="Example for Meta Characters in Regular Expression"
x=re.findall("M*",str)
print(x)


import re
str="Example for Meta Characters in Regular Expression"
x=re.findall("..r",str)
print(x)

from re import*
str="Friend in need is a friend indeed"
x=findall("ee",str)
print(x)

from re import*
str="Friend in need is a friend indeed"
x=findall("ie",str)
print(x)

from re import*
str="Friend in need is a friend indeed"
x=findall("m+",str)
print(x)

from re import*
str="Friend in need is a friend indeed"
x=findall("ie+",str)
print(x)

from re import*
str="Friend in need is a friend indeed"
x=findall("e{1}",str)
print(x)

from re import*
str="Friieend in need is a friieend iindeed"
x=findall("i{2}e{2}",str)
print(x)

import re
str="Friieend in need is a friieend iindeed"
x=re.findall("ie{2}",str)
print(x)

import re
str="Friend in need is a friend indeed"
x=re.findall("\s",str)
print(x)

import re
str="Friend in need is a friend indeed"
x=re.findall("\S",str)
print(x)

import re
str="123 Friend in need is a 456.5 friend indeed"
x=re.findall("\d",str)
print(x)

import re
str="123 Friend in need is a friend indeed"
x=re.findall("\w",str)
print(x)

import re
str="123 Friend in need is a friend indeed"
x=re.findall("\W",str)
print(x)

import re
str="123 Friend in need is a friend indeed"
x=re.findall("[^123]",str)
print(x)

a=int(input("Enter any number: "))
b=str(a)
c=len(b)
count=0
i=0
while(i<c):
    pro=(int(b[i])**c)
    count+=pro
    i+=1
print(count)
if (count==a):
    print("Number is armstrong")
else:
