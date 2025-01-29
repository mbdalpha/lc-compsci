import shelve


if input("(N)ew or (L)oad") == "N":
    # Input and store data
    name = input("Enter your name:")
    age = int(input("Enter your age:"))

    with shelve.open("data.db") as f:
        f["name"] = name
        f["age"] = age

else:
    # Load and display data
    with shelve.open("data.db") as f:
        age = f["age"]
        name = f["name"]
        print(name, age)