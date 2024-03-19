# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:10:08 2021

@author: Kashi
"""
#whileloop1 number 1
n=int(input("Enter the number= "))
i=1
while i<=n:
    print("Value= ",i)
    i=i+1
    
    
#whileloop1 number 2
n=int(input("Enter the number= "))
i=1
while i<=11:
    print(n,"x",i,"=",i*n)
    i=i+1
 
#whileloop1 number 3
n=int(input("Enter the number= "))
i=1
while i<=n:
    if(i%2==0):
        print("The number is even",i)
    else:
        print("The number is odd",i)
    i=i+1
    
#whileloop1 number 4
num = 1
n=5
while n >= 1:
     num = num * n
     n = n - 1
print(num)

#whileloop1 number 5
n=int(input("Enter the number= "))
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
    print(i,"+",end='')
print("the sum of the numbers =",s)

#whileloop1 number 6
n=int(input("Enter the number= "))
i=1
while i<=n:
    if(i==3):
        break
    else:
        print(i)
    i=i+1

#whileloop1 number 7
n=int(input("Enter the number= "))
i=1
c=0
while i<=n:
    c=c+1
    if(i<5):
        print(i," is less than 5")
    elif(i==5):
        print(i," is 5")
    else:
        print(i," is not less than 5")
    i=i+1
