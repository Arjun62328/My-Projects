# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 09:21:41 2021

@author: Kashi
"""
#--------------------------------------------------------------------
#ppt1
def add():
    x=int(input("Enter the value of x= "))
    y=int(input("Enter the value of y= "))
    print(x+y)

add()
print("\n Let's call again")
add()

def max2():
    x=int(input("Enter the value of x= "))
    y=int(input("Enter the value of y= "))
    if x>y:
        print(x," is max")
    else:
        print(y," is max")
max2()

#ppt2
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
    
a=int(input("Enter the value of a= "))
b=int(input("Enter the value of b= "))
add(a,b)
sub(a,b)
mul(a,b)
div(a,b)

#ppt3
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
    
x=int(input("Enter the value of a= "))
y=int(input("Enter the value of b= "))
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)

#ppt4
def add(a,b):
    print(a+b)
    
def max(a,b):
    if a>b:
        print(" no1 is max")
    else:
        print(" no2 is max")

def sqr(a):
    print("square = ",a*a)
    
x=int(input("Enter the value of a= "))
y=int(input("Enter the value of b= "))
add(x,y)
max(x,y)
sqr(x)

#------------------ USER DEFIEND DEFAULT ARGUMENT --------------------
#ppt5
def add(a,b,c,d,e):
    print("Add = ",a+b+c+d+e)
add(11,22,33,44,55)
add(11,22,33,44)
add(11,22,33)
add(11,22)
    
#ppt6
def add(a,b,c=0,d=0,e=0):
    print("Add = ",a+b+c+d+e)
add(11,22,33,44,55)
add(11,22,33,44)
add(11,22,33)
add(11,22)

#ppt7
def mul(a,b,c=0,d=0,e=0):
    print("mul = ",a*b*c*d*e)
mul(11,22,33,44,55)
mul(11,22,33,44)
mul(11,22,33)
mul(11,22)

#ppt8
def mul(a,b,c=1,d=1,e=1):
    print("mul = ",a*b*c*d*e)
mul(11,22,33,44,55)
mul(11,22,33,44)
mul(11,22,33)
mul(11,22)
    
#------------------ USER DEFIEND KEYWORD ARGUMENT --------------------
#ppt9
def data(name,no,age):
    print("name= ",name,"age= ",age,"no= ",no)
data("ram",1,21)
data(age=22,name='jay',no=2)

#------------------ USER DEFIEND Arbitary ARGUMENT --------------------
#ppt10
def data(*name):
    for x in name:
        print(x)
data('ram','raj','arjun','jay')
print("*"*20)
data('ram','raj','arjun')    
    
#ppt11
def pdata(*a):
    print("\n Values")
    for no in a:
        print(no,"End= ")
pdata(11,22,33,44)
pdata(10,20)

#------------------ USER DEFIEND RETURN STATEMENT --------------------
#ppt12
def max2(x,y):
    if x>y:
        return x
    else:
        return y
def sqr(x):
    print("square= ",x*x)
ans=max2(10,5)
sqr(ans)

#ppt13
def cal(x,y):
    return x+y,x-y,x*y,x/y
a,s,m,d=cal(22,2)
print("add  = ",a)
print("sub= ",s)
print("mul = ",m)
print("div =",d)

    
#-------------------- function text file programs ----------------------
#1
def max3():
    x=int(input("Enter the value of x= "))
    y=int(input("Enter the value of y= "))
    z=int(input("Enter the value of z= "))
    if x>y:
        print(x," is max")
    elif y>z:
        print(y," is max")
    else:
        print(z," is max")
        
max3()

#2 first method
def add():
    x=int(input("Enter the value of x= "))
    y=int(input("Enter the value of y= "))
    print(x+y)

add()
#2 second method
def add(x,y):
    print(x+y)
    
x=int(input("Enter the value of x= "))
y=int(input("Enter the value of y= "))
  
add(x,y)

#3
def mul(*a):
    r=1
    for i in a:
        r=r*i
    print(r," is the multipilcation of the list")

mul(2,3,4,5,6)

#4
def fac(x):
    
    if x==0:
        return 1
    else:
        return x*fac(x-1)
x=int(input("Enter the value u want to get the factorial of = "))   
print(fac(x))
    
    


#5
def oddeven():
    x=int(input("Enter the value u want to check odd even= "))
    if(x%2==0):
        print(x," is even")
    else:
        print(x," is odd")

oddeven()
 
#6
def test_range(n):
    if n in range(3,9):
        print( n," is in the range")
    else :
        print("The number is outside the given range.")
test_range(10)


#7
def string(s):
    dict={'Upper_Case':0,'Lower_Case':0}
    for x in s:
        if x.isupper():
            dict['Upper_Case']+=1
        else:
            dict['Lower_Case']+=1
    print(s)
    print(dict['Upper_Case'])
    print(dict['Lower_Case'])

string('Arjun')









def is_leap(i):
    if i%400==0:
        return True
    else:
        return False
i=int(input(" Enter year = "))
is_leap(i)

    
    
    
    
    
    
    
    
