def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))

print("Sum:", addition(num1,num2))
print("Difference:",subtraction(num1,num2))
print("Product:",multiplication(num1,num2))
print("Quotient:",division(num1,num2))