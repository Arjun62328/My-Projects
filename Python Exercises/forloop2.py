#forloop2 number 1
n=int(input("Enter the number you want = "))
s=0
for i in range(1,n+1):
    s=s+i
    x=i*i
    if(i%2==0):
        print(x,"+",end='')
    else:
        print(x,"-",end='')

    
print("\nThe sum of the numbers is ",s)


#forloop2 nummber 2
n=int(input("Enter the number you want = "))
s=0
for i in range(1,n+1):
    
    if(i%2==0):
        print("",end='')
    else:
        s=s+i
        print(i,"+",end='')

    
print("\nThe sum of the numbers is ",s)



#forloop2 number 3
n=int(input("Enter the number you want = "))
s=0
x=0
z=1
for i in range(1,n+1):
    s=s+(1/i)
    x=x+1
    print(z,"/",x,"+",end='')
print(round(s,2))


#forloop2 number 4
num = int(input("Enter a number: "))

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       print(i,"X ",end='')
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)



#forloop2 number 5
start = 11
end = 25
  
for i in range(start, end+1):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i,end=' ')
#forloop2 number 6
n=int(input("Enter the number you want = "))  

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
#forloop2 number 7
n=int(input("Enter the number you want = "))  

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#forloop2 number 8
n=int(input("Enter the number you want = "))
x=0
for i in range(1,n+1):
    for j in range(1,i+1):
        x=x+1
        print(x,end=' ')
    print()
    
#forloop2 number 9
n=int(input("Enter the number you want = "))
x=0
for i in range(1,n+1):
    for j in range(0,i+1):
        x=i+1
        print(x,end='')
    print()


#forloop2 number 10
n=int(input("Enter the number you want = "))
x=1
for i in range(1,n+1):
    for j in range(1,i+1):
        x=i-j
        print(x,end='')
    print()
        
#forloop3 number 1
n=int(input("Enter the number you want = "))  

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
    
#forloop3 number 2    
n = int(input("Enter a number: "))  
for i in range(1,n):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()

      
#forloop3 number 3
n = int(input("Enter a number: "))  
for i in range(n,0,-1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    
#forloopnumber 4
n = int(input("Enter a number: "))  
for i in range(1,n):
    for k in range(1,n-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
    
#forloop3 number 5
n = int(input("Enter a number: "))  
for i in range(n,0,-1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
    
#forloop3 number 6
n=int(input("Enter the number you want = "))  
x=0
for i in range(1,n+1):
    x=x+1
    for j in range(1,n):
        print(x,end=" ")
    print()
    
#forloop3 number 7
n=int(input("Enter the number you want = "))  
for i in range(1,n+1):
    x=0
    for j in range(1,n+1):
        x=x+1
        print(x,end=" ")
    print()
    
#forloop3 number 8    
n=int(input("Enter the number you want = "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1) or (i==n) or (j==1) or (j==n):
            print("*",end='')
        else:
            print(" ",end='')
            
    print()
    
#forloop3 number 9
n = int(input("Enter a number: "))  
for i in range(1,n+1):
    for k in range(1,n+1-i):
        print(" ",end="")
    for j in range(1,(2*i-1)+1):
        print("*",end="")
    print()
for a in range(1,n+1):
    for b in range(1,n+1):
        if(a==1) or (a==n) or (b==1) or (b==n):
            print("* ",end='')
        else:
            print(" ",end=' ')

    print()


#forloop3 number 10
for i in range(8):
    for j in range(6):
        if(j==0) or (j+i==4 and i<4) or (j==i-2 and i>3):
            print("*",end=' ')
        else:
            print(end=' ')
    print()
            

        
    


    



    





        
        
        
    
    
    
    
    
    
    