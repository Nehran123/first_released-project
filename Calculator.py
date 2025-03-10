operation= input("Choose +,-,*,/")
num1=int(input("Enter a number= "))
num2=int(input("Enter another number= "))

def addition(num_1,num_2):
    return num_1 + num_2



def subtraction(num1,num2):
    return num1-num2



def multiplication(num1,num2):
    return num1*num2



def division(num1,num2):
    return num1/num2


if operation=="+":
    result= addition(num1,num2)

elif operation=="-":
    result= subtraction(num1,num2)

elif operation=="*":
    result= multiplication(num1,num2)

elif operation=="/":
    result= division(num1,num2)

print("result is", result)
