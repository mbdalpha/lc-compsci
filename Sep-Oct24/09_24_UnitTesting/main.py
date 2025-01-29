
def convert(text):
    if not text.isdigit():
        print("Text contained non-digit characters")
        exit()
    return int(text)

def add(num1, num2):
    return num1 + num2

print(convert("234"))
print(add(4, 9))