#1 explanation
 print(22/0)
 
 
 a=int(input("Enter a"))
 b=int(input("Enter b"))
 
 ans=a/b
 print(ans)
 
 
 #2
 
 try:
      a=int(input("Enter a"))
      b=int(input("Enter b"))
 
      ans=a/b
      print(ans)
except:
    print("Error")
    

#3 

try:
    a=int(input("Enter a"))
    b=int(input("Enter b"))
 
    ans=a/b
    print(ans)
except ZeroDivisionError:
    print("Biddu why u entered 0")
    
except ValueError:
    print("Why u entered characters in division ")
except:
    print("Other erorr")
    
#4
try:
    a=int(input("Enter a"))
    b=int(input("Enter b"))
    
    if a<0:
        print("Erorr valid number in english")
    elif b<0:
        print("Error valid nuynbber in hindi")
        
    else:
        ans=a+b
        print("Total marks = ",ans)
except:
    print("other error")
    
#5

class marks(Exception):
    pass
try:
    a=int(input("Enter marks of a "))
    b=int(input("Enter the value of B"))
    if a<0:
        raise marks
    elif b<0:
        raise marks
    else:
        ans=a+b
        print("Total Marks = ",ans)
except marks:
    print("Please enter valid marks")
except:
    print("Other error")
    
#6
