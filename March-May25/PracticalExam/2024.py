# Question 16(a)
# Examination Number:
from random import choice

fruits = ['apple', 'cherry', 'orange']

random_fruit_1 = choice(fruits)
random_fruit_2 = choice(fruits)
random_fruit_3 = choice(fruits)

print(f"Random Fruit 1: {random_fruit_1}")
print(f"Random Fruit 2: {random_fruit_2}")
print(f"Random Fruit 3: {random_fruit_3}")
print("")
##print(f"First fruit is {random_fruit_1}")
##if random_fruit_1 == random_fruit_2:
##    print("First pair match")
##    if random_fruit_1 == 'cherry':
##        print("First pair are cherries")

if random_fruit_1 == random_fruit_2 or random_fruit_1 == random_fruit_3 or random_fruit_2 == random_fruit_3:
    print("Matching pair")
    print("")

x = 0
a = 0
c = 0
o = 0
while x < 100:
    x += 1
    rand_f = choice(fruits)
    if rand_f == "apple":
        a += 1
    if rand_f == "cherry":
        c += 1
    if rand_f == "orange":
        o += 1

print(f"apple {a} \ncherry {o} \norange {31}")
print("")
print("")
print("")

# Question 16(b)
# Examination Number:

fruits = ['apple', 'cherry', 'orange']
print(f"The initial list of fruits is: \n{fruits}")
fruits.append(input("Enter an additional fruit: "))
print(f"The list of four fruits is: \n{fruits}")

x = 0
nom = ""
while x == 0:
    nom = input("Nominate your winning fruit: ")
    if not nom in fruits:
        print("That is not one of the fruits you can choose from.")
    else:
        x += 1
        print(f"The winning fruit you selected is {nom}")

x = 0
i = 0
while x == 0:
    f1 = choice(fruits)
    f2 = choice(fruits)
    f3 = choice(fruits)

    if nom == f1 and nom == f2 and nom == f3:
        print(f"Winner after {i} tries")
        x += 1
    i += 1