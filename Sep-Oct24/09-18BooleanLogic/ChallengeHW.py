import statistics

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def selector():
    program = input("Type here: ")
    if program == "1":
        age_next_year()
    elif program == "2":
        num_compare()
    elif program == "3":
        age_compare()
    else:
        print("Please input a number from the above list")
        selector()


def age_next_year():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    person1 = Person(name, age)
    print(f"Next year {person1.name} will be {person1.age + 1}")

def num_compare():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"The sum is {num1 + num2}")
    print(f"The product is {num1 * num2}")
    print(f"The average is {statistics.mean([num1, num2])}")

def age_compare():
    i=0
    order = "first"
    while i <= 1:
        name = input(f"Enter {order} name: ")
        age = int(input(f"Enter {name}'s age: "))
        if i == 0:
            person1 = Person(name, age)
            order = "second"
        else:
            person2 = Person(name, age)
        i += 1

    if person1.name.lower() == person2.name.lower():
        print("The names are the same!")
        print("Please use a different name for each person!")
        age_compare()
        exit()

    if person1.age == person2.age:
        print(f"{person1.name} and {person2.name} are the same age.")
    elif person1.age > person2.age:
        print(f"{person1.name} is the oldest.")
    else:
        print(f"{person2.name} is the oldest")

print("Welcome to my application")
print("Please select from the following list by typing in the corresponding number:\n"
      "1. Age next year calculator\n"
      "2. Number comparer\n"
      "3. Age comparer")
selector()

