start = int(input("enter a start number:"))
end = int(input("enter a end number:"))
count = 0
for i in range(start, end + 1):
    if i % 3 == 0:
        count = count + 1
print(f"Divisible by 3: {count}")