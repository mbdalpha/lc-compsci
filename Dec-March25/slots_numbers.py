import random

def spin():
    x = random.randint(1,7)
    y = random.randint(1,7)
    z = random.randint(1,7)
    return x, y, z

x, y, z = spin()

total = 0
while not (x == y and y == z):
    x, y, z = spin()
    total +=1
    
print(total)

