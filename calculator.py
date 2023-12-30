#Task 2- Program to design a simple calculator with basic arithmetic operations
print("*****Here's a simple calculator*****")
print("Enter two numbers:")
num1=int(input())
num2=int(input())
print("Enter you operation choice:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent")
ch=int(input())
print("The two numbers are:",num1,"and",num2)
match ch:
    case 1:
        print("The addition of ",num1,"and",num2,"is:",num1+num2)
    case 2:
        if(num1>num2):
            print("The difference of ",num1,"and",num2,"is:",num1-num2)
        else:
            print("The difference of ",num1,"and",num2,"is:",num2-num1)
    case 3:
        print("The product of ",num1,"and",num2,"is:",num1*num2)
    case 4:
        if(num2!=0):
            print("The quotient of ",num1,"and",num2,"is:",num1/num2)
        else:
            print("Division not possible")
    case 5:
        print("Exponent result is",num1**num2)
    case _:
        print("Wrong choice of operation")