
def input_int(msg, error_msg="Please enter only digits"):
    number = input(msg)
    while not number.isdigit():
        number = input(error_msg)
    return int(number)

print("Start")
print(input_int("Please enter a number: "))

age = input_int("Please enter your age: ", "Please enter a valid age")
print("Triple your age is", age*3, sep=",", end="")

print("Stop")