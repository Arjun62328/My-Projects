# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:11:53 2021

@author: Kashi
"""

students={1:100,2:30,3:50,4:"Ram",5:"Raj"}

for i,j in students.items():
    print (i,j)
    
for i in students:
    print(i)

students.pop(2)
students.popitem()

students[6]=20
students.setdefault(7,"kite")

marks={8:123,5:1245,'name':"kashish"}


#-----------------------------------------------------------------------
#dic1
marks={"ram":33,"rahul":45,"devesh":30,"jayul":34}
print(marks)

#dic2
for i,j in marks.items():
    print(i,j)
    
#dic3
if 'ram' in marks:
    print("yes the key exists")
else:
    print("no the key doesnt exists")
    
#dic4
marks={"ram":33,"rahul":45,"devesh":30,"jayul":15}
for i,j in marks.items():
    if(j>=18):
        print(i,j,"passed")
    else:
        print(i,j,"Failed")
#dic5
marks={"ram":33,"rahul":45,"devesh":30,"jayul":15}
sum=0
for i,j in marks.items():
    sum=sum+j
    
print(sum)

#dic6
marks={"ram":33,"rahul":45,"devesh":30,"jayul":15}
del marks["ram"]
print(marks)
    