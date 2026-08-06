text = input("enter text:")
count = 0
for i in text:
    if i in "aeiou":
        count = count + 1
print(f"vowel count: {count}")