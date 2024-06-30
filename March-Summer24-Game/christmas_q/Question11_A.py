# Question 11 
# Examination Number:  
from random import randint 
print("Dice simulation program and analysis program")
results = [] 
frequencies = [0, 0, 0, 0, 0, 0] 
 
# Loop 100 times 
for i in range (100): 
    throw_result = randint(1,6) # store a random value between 1 and 6 
    results.append(throw_result) # append each value to results 
 
    # Start to build up a list of frequencies for each value thrown
    frequencies[throw_result - 1] = frequencies[throw_result - 1] + 1

print()
#print("Results:", results)
print("Frequencies:", frequencies)
print("Dice Frequencies")
print("---- -----------")
for i in range(0,6):
    print(i+1, "  ", frequencies[i])

print()
max_value = max(frequencies)
print(frequencies.index(max_value) + 1, "was rolled the most often (" + str(max_value), "times)")


def print_stars(number):
    for i in range(0, number):
        print("*", end="")


print()

for i in range(0, 6):
    print_stars(frequencies[i])
    print()


# HW: Method 2 - Ask Eric for code
# use '.remove' after each drawing - Try entirely from scratch (drum draw 1-10)