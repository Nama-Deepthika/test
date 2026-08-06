number = int(input("enter a number:"))
sum = 0
num = number
while num > 0:
    digit = num % 10 
    sum += digit
    num = num // 10
print(f"Sum of ditits: {sum}") 
