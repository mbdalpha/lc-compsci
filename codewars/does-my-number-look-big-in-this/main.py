def narcissistic(value):
    string = str(value)
    length = len(string)
    total = 0
    for num in string:
        total += int(num)**length
    return value == total


print(narcissistic(371), "True")
print(narcissistic(7), "True")
print(narcissistic(122), "False")
print(narcissistic(4887), "False")
