#factorial funtion
def fact(num):
    if num==1:
         return num
    else:

     return num*fact(num-1)
    
n=int(input("enter a number"))
if n<=0:
     print("sorry connot fint the factorial of 0 or less than 0")
else:
     print(" factorial of ",n," is ",fact(n))
