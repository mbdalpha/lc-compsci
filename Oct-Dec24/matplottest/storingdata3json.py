import json


if input("(N)ew or (L)oad") == "N":
    # Input and store data
    name = input("Enter your name:")
    age = int(input("Enter your age:"))

    with open("data.json", "w") as f:
        d = {"name":name,"age":age}
        json.dump(d, f)

else:
    # Load and display data
    with open("data.json", "r") as f:
        d = json.load(f)
        print(d["name"], d["age"])