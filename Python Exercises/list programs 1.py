# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:11:23 2021

@author: Kashi
"""
#umber 1
list=[11,44,500,22,99,77,200,66,2]
x=sum(list)
print(x)



#umber 2
list=[11,44,500,22,99,77,200,66,2]
for x in list:
    if(x%2==0):
        print(x)
   
    
#umber 3

list=[11,44,500,22,99,77,200,66,2]
for x in list:
    if(x%2==0):
        print(x," is even ")
    else:
        print(x," is odd")
        
#number 4
list=[11,44,500,22,99,77,200,66,2]
print(max(list))

#number 5
list=[11,44,500,22,99,77,200,66,2]
print(min(list))

#number 6
list=[11,44,500,22,99,77,200,66,2]
print(list[0]+list[-1])

#number 7
list=[11,44,500,22,99,77,200,66,2]
list.sort()
print(list)

#number 8
list=[11,44,500,22,99,77,200,66,2]
list.reverse()
print(list)

#number 9
list=[11,44,500,22,99,77,200,66,2]
list.sort()
print(list," is asc")
x=list
x.reverse()
print(x," is desc")

#number 10
list=[11,44,500,22,99,77,200,66,2,500,99]
x=[]
for i in list:
    if i not in x:
        x.append(i)
print(x)
    
#number 11
list=[11,44,500,22,99,77,200,66,2]
c=0
for i in list:
    if(i==[]):
        print('The list is empty')
    else:
        c=c+1
print("There are total ",c," elements in the list")

#number 12
list=[11,44,500,22,99,77,200,66,2,2,11]
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)

#number 13
list=[11,44,500,22,99,77,200,66,2,2,11]
n=int(input("Enter the value u want greater from= "))
for i in list:
    if(i>n):
        print(i)
    

#number 14
list=[11,-44,500,22,-99,-77,-200,66,2]
x=[]
for i in list:
    i=i*-1
    x.append(i)
print(x)


#number 15
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


#number 16
num = [11,44,500,22,99,77,200,66,2,2,11]
num = [x for x in num if x%2!=0]
print(num)

#number 17
list=[]
n=int(input("Enter The number u want sqaure of in odd= "))
for x in range (1,n+1):
    if(x%2!=0):
        x=x*x
        list.append(x)
print(list)


#number 18
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)

#number 19
 #method 1
list1=[1,2,3,4,5]
list2=[1,3,8,5,10]
x=[]
for i in list1:
    if i in list2:
        x.append(i)
print(x)
 # method 2
list1 = [1, 2, 3, 0,77,66]
list2 = [77,200,66,2,11,22]
list(set(list1) & set(list2))


#number 20
list1 = [1, 2, 3, 0,77,66] 
list2=[77,200,66,2,11,22]
for i in list2:
    
    list1.append(i)
    
    
print(list1)

















