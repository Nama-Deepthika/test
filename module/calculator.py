num1 = int(input("num1:"))
num2 = int(input("num2:"))
operator = input("enter the operator(+, -, *, /):")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("invalid operator")
