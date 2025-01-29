
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

if (first > second and first < third) or (first < second and first > third):
    print(f"{first} does lie between {second} and {third}")
else:
    print(f"{first} does not lie between {second} and {third}")


s = 0
n = 0

data = [4, 7, 19, 3, 56, 39, 67, 32, 9]
for n in data:
    if not n % 2 == 0:
        s += n
print(s)


m = 0
n = 0

data = [4, 7, 19, 3, 56, 39, 67, 32, 9]
for n in data:
    if not n % 2 == 0:
        m = n
print(s)
