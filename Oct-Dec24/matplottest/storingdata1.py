
if input("(N)ew or (L)oad") == "N":
    # Input and store data
    name = input("Enter your name:")
    age = int(input("Enter your age:"))

    f = open("data.txt", "w")
    f.write(name + "\n")
    f.write(str(age) + "\n")
    f.close()

else:
    # Load and display data
    with open("data.txt", "r") as f:
        name = f.readline()
        age = int(f.readline())
        print(name, age)