print("Welcome to my Calculator app!")
num1=int(input("Please Enter the First Number: "))
num2=int(input("Please Enter the Second Number: "))
operator = input("Please Enter the operator sign:(+,-,*,/)")
if operator == '+':
    Result=num1+num2
elif operator == '-':
    Result=num1-num2
elif operator == '*':
    Result=num1*num2
elif operator == '/':
    Result=num1/num2
else:
    print("Error")
print("Result: "+str(Result))
