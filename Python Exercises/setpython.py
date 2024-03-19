# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:01:16 2021

@author: Kashi
"""
#union
A={1,2,3,4}
B={4,5,6,7}
C=A|B
print(C)
print(A.union(B))

#intersect
c=A&B
print(c)
print(A.intersection(B))

#Difference
c=B-A
print(c)

#Isdisjoint()
A={1,2,3}
B={4,5,6}
print(A.isdisjoint(B))

#issubset
A={1,2,3}
B={1,2,3,4,5}
C={1,2,4,5}
print(A<B)
print(B<C)
print(A<C)


#issuperset
A={1,2,3}
B={1,2,3,4,5}
C={1,2,4,5}
print(A>B)
print(C<B)
print(A<C)

#-----------------------------------------------------------------------
#set1
a={11,22,33,44,55}
print(a)

#set2
for i in a:
    print(i)
    
#set3
a={11,22,33,44,55}
a.add(66)
print(a)

#set4
a={11,22,33,44,55}
a.remove(33)
print(a)

#set5
a={11,22,33,44,55}
b={44,55,66,77,88}
c=a&b
print(c)

#set6
a={11,22,33,44,55}
b={44,55,66,77,88}
c=a|b
print(c)

#set7
a={11,22,33,44,55}
b={44,55,66,77,88}
c=a-b
print(c)

#set8
a={11,22,33,44,55}
b={44,55}
print(A<B) 

#set9
a={11,22,33,44,55}
b=a
a=a-b
print(a)

#set10
a={11,22,33,44,55}
b=max(a)
c=min(a)
print(b," is the max value in set")
print(c," is the min value in set")

