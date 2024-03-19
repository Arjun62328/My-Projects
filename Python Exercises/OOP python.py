# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:22:01 2021

@author: Kashi
"""

#ppt 1
class student:
    def __init__(self):
        self.name='Ram'
        self.rollno=12
    
    def printdata(self):
        print("Name = ",self.name," Roll no = ",self.rollno)

s1=student()
s2=student()
s1.printdata()
s2.printdata()

#ppt 2
class emp:
    def __init__(self,eno,ename,salary):
        self.ename=ename
        self.eno=eno
        self.salary=salary
        
    def printdata(self):
        print("Name = ",self.ename," No = ",self.eno," Salary = ",self.salary)

e1=emp(11,'Ram',20000)
e2=emp(12,'Raj',19000)
e3=emp(13,'harsh',21000)
e1.printdata()
e2.printdata()
e3.printdata()

#ppt3

class stu:
    def __init__(self,no,name):
        self.no=no
        self.name=name
        print(self)
    def printdata(self):
        print("self = ",self," no = ",self.no," name = ",self.name)
        
s1=stu('Ram',1)
s2=stu('raj',2)
s1.printdata()
s2.printdata()

#ppt4 
class math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def printdata(self):
        print("A = ",self.a," B = ",self.b)
    def add(self):
        print("Add = ",self.a+self.b)
    def sub(self):
        print("sub = ",self.a-self.b)
    def mul(self):
        print(" mul  = ",self.a*self.b)
    def div(self):
        print(" Div = ",self.a/self.b)
        
m1=math(22,2)
m1.printdata()
m1.add()
m1.sub()
m1.mul()
m1.div()

#ppt5 
class stu():
    def __init__(self):
        self.ename=""
        self.no=0
        self.salary=0
    def setdata(self):
        self.ename=input("Enter the name =")
        self.eno=int(input("Enter the number = "))
        self.salary=int(input("Enter the salary = "))
    def printdata(self):
        print("\nName = ",self.ename," no = ",self.eno," Salary = ",self.salary)

s1=stu()
s2=stu()
s1.setdata()
s2.setdata()
s1.printdata()
s2.printdata()

#ppt6 
class bank():
    def __init__(self,acno,acname,balance):
        self.acno=acno
        self.acname=acname
        self.balance=balance
    def printdata(self):
        print("Account name= ",self.acname," Account no= ",self.acno," Balance= ",self.balance)
    def deposit(self):
        n=int(input("Enter the amount u want to deposit= "))
        self.balance=self.balance+n
    def withdraw(self):
        a=int(input("Enter the amount u want to withdraw= "))
        if(self.balance>a):
            self.balance=self.balance-a
        else:
            print("\nItna hai tere pass ???")
            
        
        
    
b1=bank(1,"Ram",20000)
b1.printdata()
b1.deposit()
b1.printdata()
b1.withdraw()
b1.printdata()


#ppt7
class stu:
    
   def __init__(self,no,name,marks):
    self.no=no
    self.name=name
    self.marks=marks

   def printdata(self):
    print("No= ",self.no,"Name = ",self.name)
    for x in self.marks:
        print(x)
        
   def printtotal(self):
    print("total = ",sum(self.marks))

s1=stu(1,'ram',[22,21,19])
s2=stu(2,'raj',[23,20,21])
s1.printdata()
s2.printdata()
s1.printtotal()
s2.printtotal()

#ppt8
class stu:
    
    
   def __init__(self):
    self.no=0
    self.name=""
    self.x=3
    self.marks=[]

   def setdata(self):
       
       self.no=int(input("Enter no= "))
       self.name=input("Enter name = ")
       for i in range(1,self.x+1):
           y=int(input("enter marks= "))
           self.marks.append(y)
   def printdata(self):
    print("No= ",self.no,"Name = ",self.name)
    for m in self.marks:
        print(m)
        
   def printtotal(self):
    print("total = ",sum(self.marks))

s1=stu()
s2=stu()
s1.setdata()
s2.setdata()
s1.printdata()
s2.printdata()
s1.printtotal()
s2.printtotal()


#ppt9
class student:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def __del__(self):
        print("destruction Started")
    def printdata(self):
        print("no= ",self.no,"name = ",self.name)

s1=student(1,'ram')
s2=student(2,'raj')
s1.printdata()
s2.printdata()
del s1
del s2
s1.printdata()
s2.printdata()

#==================== INHERITANCE ====================================
#inheritance 1 ( Single inheritance )
class sheru:
    def show(self):
        print("hi, i am parent class")

class monty(sheru):
    def display(self):
        print("Hi , i am child class ")

m1=monty()
m1.display()
m1.show()

#inheritance 2 (multilevel inheritance without values )
class sheru:
    def show(self):
        print("hi i am parent class")

class monty(sheru):
    def display(self):
        print("hi i am parent class of third class")

class romeo(monty):
    def printfinal(self):
        print("hi i am the child class ")
        
r1=romeo()
r1.show()
r1.display()
r1.printfinal()

#inheritance 3 ( multilevel inheritance with values but without argument)

class stu:
    def __init__(self):
        self.no=5
        self.name="ram"
    def showstu(self):
        print("no = ",self.no,"name = ",self.name)

class marks(stu):
    def __init__(self):
        stu.__init__(self)  #important to get init values of class 1/ stu
        self.eng=50
        self.hindi=30
    def printmarks(self):
        print("Eng mark= ",self.eng,"hindi marks= ",self.hindi)

class result(marks):
    def __init__(self):
        marks.__init__(self)
    def printresult(self):
        print("Total = ",self.eng+self.hindi)
        
r1=result()
r1.showstu()
r1.printmarks()
r1.printresult()


#inheritance 4 ( multilevel inheritance with values by argument )

class stu():
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def showstu(self):
        print("no= ",self.no,"name = ",self.name)

class marks(stu):
    def __init__(self,no,name,eng,hindi):
        stu.__init__(self, no, name)
        self.eng=eng
        self.hindi=hindi
    def printmarks(self):
        print("eng = ",self.eng,"hindi = ",self.hindi)

class result(marks):
    def __init__(self, no, name, eng, hindi):
        marks.__init__(self, no, name, eng, hindi)
    def printresult(self):
        print("Total = ",self.eng+self.hindi)
        
r1=result(1,'ram',33,35)
r1.showstu()
r1.printmarks()
r1.printresult()

#inheritance 5 ( Multiple interitance many base class 1 derivev class)

class stu:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def showstu(self):
        print("no= ",self.no,"name = ",self.name)

class marks:
    def __init__(self,eng,hindi):
        self.eng=eng
        self.hindi=hindi
    def printmarks(self):
        print("eng = ",self.eng,"hindi = ",self.hindi)
        
class result(stu,marks):
    def __init__(self,no,name,eng,hindi):
        stu.__init__(self, no, name)
        marks.__init__(self, eng, hindi)
        
    def printresult(self):
        print("Total = ",self.eng+self.hindi)
        
r1=result(1,'ram',11,11)
r1.showstu()
r1.printmarks()
r1.printresult()

        

#inheritance  6 ( Hierarchical inheritance )
class poly:
    def __init__(self,h,w):
        self.h=h
        self.w=w
        
class tri(poly):
    def __init__(self,h,w):
        poly.__init__(self,h,w)
    def printarea(self):
        print("Area of triangle = ",self.h*self.w*0.5)

class rect(poly):
    def __init__(self,h,w):
        poly.__init__(self,h,w)
    def printrect(self):
        print("Area of rect = ",self.h*self.w)
        
t1=tri(100,200)
t1.printarea()
r1=rect(100,200)
r1.printrect()

#inheritance 7 ( Hybrid Inheritance , Diamond Inheritance )
class stu:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def showstu(self):
        print("No = ",self.no,"Name = ",self.name)

class marks(stu):
    def __init__(self,eng,hindi):
        self.eng=eng
        self.hindi=hindi
    def printmarks(self):
        print("Eng marks = ",self.eng,"Hindi marks = ",self.hindi)

class sports(stu):
    def __init__(self,cricket):
        self.cricket=cricket
    def showsports(self):
        print("cricket = ",self.cricket)
        
class result(marks,sports):
    def __init__(self,no,name,eng,hindi,cricket):
        stu.__init__(self,no,name)
        marks.__init__(self,eng,hindi)
        sports.__init__(self,cricket)
    def printresult(self):
        print("Total = ",self.eng+self.hindi)

r1=result(11,"ram",22,33,50)
r1.showstu()
r1.printmarks()
r1.showsports()
r1.printresult()


#inheritance 8 ( SUPER FUNCTION )

class a:
    def methodA(self):
        print("A is class ")

class b(a):
    def methodB(self):
        super().methodA()
        print("B class")

b=b()
b.methodB()


#======================= EPO ==================================
# 1 polymorphisum
class india():
    def capital(self):
        print("New Delhi is the capital of India")
        
    def language(self):
        print("Hindi is the national language off India)")
    
    def type(self):
        print("India is a developing country ")

class USA():
    def capital(self):
        print("Washington DC is the  capital of the USA")
    def language(self):
        print("English is the national language of USA ")
    def type(self):
        print("USA is a developed country")

i1=india()
u1=USA()
for country in (i1,u1):
    country.capital()
    country.language()
    country.type()
    
#2 polymorphisum in Inheritance

class bird:
    def intro(self):
        print("There are many types of birds")
    def flight(self):
        print("Most of the birds can fly but some cannot")

class sparrow(bird):
    def flight(self):
        print("Sparrows can fly")

class ostrich(bird):
    def flight(self):
        print("Ostriches cannot fly")
        
b1=bird()
s1=sparrow()
o1=ostrich()

b1.intro()
b1.flight()
s1.flight()
o1.flight()

#3 ENCAPSULATION ( public private protected class)

class base:
    def __init__(self):
        self._a=2         # self_ = protected member
        
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("Calling protected member of base class")
        print(self._a)

b1=base()
d1=derived()

print(b1._a)        

#4 encapsulation 
class base:
    def __init__(self):
        self._a=2 
        self.__c=3      # self.__ = private member

class derived(base):
    def __init__(self):
        base.__init__(self)
        print("Calling a private member of base class ")
        print(self.__c)
    
b1=base()
print(b1.self.__c)

#5 data absruction 
from abc import ABC, abstractmethod

class polygon(ABC):
    def sides(self):
        pass
    
class triangle(polygon):
    def sides(self):
        print(" i have 3 sides")
    

class pentagon(polygon):
    def sides(self):
        print("i have 5 sides")

class hexagon(polygon):
    def sides(self):
        print(" i havev 6 sides")

class quadrilateral(polygon):
    def sides(self):
        print("I have 4 sides")
        
t1=triangle()
t1.sides()

t1=pentagon()
t1.sides()

k1=hexagon()
k1.sides()

k1=quadrilateral()
k1.sides()

#6 data abstraction

import abc
class parent:
    def geeks(self):
        pass

class child(parent):
    def geek(self):
        print("child class")
        
print( issubclass(child,parent))
print ( isinstance(child(),parent))


#7 data abstraction

import abc
from abc import ABC, abstractmethod

class r(ABC):
    def rk(self):
        print("Abstract cbase lass")

class k(r):
    def rk(self):
        super().rk()
        print("Subclass ")

r1=k()
r1.rk()
        
        
        
        
        
        
        













        