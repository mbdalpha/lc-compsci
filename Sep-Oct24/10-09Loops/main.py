msg = "Please enter an age, negative when finished:"
ages = []

while True:
    entered_age = int(input(msg))
    if entered_age < 0:
        break
    ages.append(entered_age)

t = 0
for age in ages:
    t += age
    m = t/len(ages)
print(f"The average is {m}")

ages.sort()
print(ages)

