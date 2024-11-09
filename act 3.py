#calculator
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def div(a,b):
    return a//b

def subtract(a,b):
    return a-b

n1=int(input("enter first number"))
n2=int(input("enter second number"))
print(" sum of ",n1," and ",n2," is",add(n1,n2))
print(" multiply of ",n1," and ",n2," is",multiply(n1,n2))
print(" quotient of ",n1," and ",n2," is",div(n1,n2))
print(" subtract of ",n1," and ",n2," is",subtract(n1,n2))
