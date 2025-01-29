
a_text = input("Enter number 1:")
if not a_text.isdigit():
    print("Please enter only digits, eg. 123")
    exit()

a = int(a_text)

b = int(input("Enter number 2:"))

if a == b:
    print("Both numbers were equal!")
else:
    print("Both numbers are different")