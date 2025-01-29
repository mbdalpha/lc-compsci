# Question 16(c)
# Name: [REDACTED]

def largest2(ls):
    l = []
    l = l + ls
    f_largest = max(l)

    while l.count(f_largest) > 0:
        l.remove(f_largest)
    s_largest = max(l)

    print("Largest:", f_largest)
    print("Second Largest:", s_largest)


def find_nth_largest(n, list_of_values):
    largest = max(list_of_values)

    while n > 1:

        while list_of_values.count(largest) > 0:
            list_of_values.remove(largest)

        n = n - 1

        largest = max(list_of_values)

    return largest


bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
obese_counter = 0

for weight in bmi_values:
    if 30 <= weight:
        obese_counter += 1

print("Obese:", obese_counter)
largest2(bmi_values)
print(find_nth_largest(3, bmi_values))
