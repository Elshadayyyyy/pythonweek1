print("this is my week 1 submission for python")
print("all u have to do is enter ur numbers and operation like +,-,*,/")

num1 = float(input("enter ur first number "))
num2 = float(input("enter ur second number "))
ope = input("what type of opration do u want to ")

if ope == "addition" or ope == "+":
    print(num1, "+", num2, "=",num1 + num2)
elif ope == "subtraction"  or ope == "-":
    print(num1, "-", num2, "=",num1 - num2)
elif ope == "multiplication" or ope == "*":
    print(num1, "*", num2, "=",num1 * num2)
elif ope == "division" or ope == "/":
    print(num1, "/", num2, "=", num1 / num2,)
else:
    print("please rerun it and choose from the basic operations")
    