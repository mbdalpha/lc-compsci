previous = []
while True:
    x = input("Enter a letter")
    if x not in previous:
        previous.append(x)
        print(str(previous))
    else:
        print("You entered that already")