# Question 16(b)
# Name: [REDACTED]

from random import *

heights = []  # an empty list of heights
weights = []  # an empty list of weights
bmi_values = []  # an empty list of bmi values


def bmi(i):
    b = round(weights[i] / (pow(heights[i], 2)) * 10000, 1)
    return b


n = int(input("Enter the number of pairs of values you wish to generate: "))

# Loop to build up the lists with random values
for count in range(n):
    # a random integer between 150 and 210
    heights.append(randint(150, 210))
    # a random integer between 50 and 130
    weights.append(randint(50, 130))

for i in range(n):
    bmi_values.append(bmi(i))

# Display the lists
print("Heights:", heights)
print("Weights:", weights)
print("BMI values:", bmi_values)
