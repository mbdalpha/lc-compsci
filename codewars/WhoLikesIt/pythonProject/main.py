
def likes(names):
    lenght = len(names)
    d_string = ""
    if lenght >= 4:
        d_string += names[0] + ", " + names[1] + " and " + str(lenght-2) + " others"
    elif lenght == 3:
        d_string += names[0] + ", " + names[1] + " and " + names[2]
    elif lenght == 2:
        d_string += names[0] + "and " + names[1]
    elif lenght == 1:
        d_string += names[0]
    else:

        d_string += "no one"

    if lenght > 2:
        d_string += " like this"
    else:
        d_string += " likes this"

    return d_string


print(likes([]), 'no one likes this')
print(likes(['Peter']), 'Peter likes this')
print(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')