num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
pr=input("Enter Operator(+,-,*,/,%):")
if pr=="+":
    print(num1+num2)
elif pr=="-":
    print(num1-num2)
elif pr=="*":
    print(num1*num2)
elif pr=="/":
    print(num1/num2)
elif pr=="%":
    print(num1%num2)
else:
    print("Invalid")

