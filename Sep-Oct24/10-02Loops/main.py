#age = input("Enter your age: ")
#while not age.isdigit(): #checks if input is a digit
#    age = input("ENTER ONLY DIGITS STUUUUUPIDDDD: ")
#print(f"Next year you will be {int(age) + 1}.")

##counting using while
#start = 1
#while start <= 10:
#    print(start)
#    start += 1

##counting using range
#for value in range(1, 11):
#    print(value)

##print out name one letter at a time
#name = input("Enter your name: ")
##print(len(name))
##or index in range(0,len(name)):
##   print(name[index])

#for letter in name:
#    print(letter)



#print out even numbers up to and including user's input

#while method
length = int(input("Please input your number: "))
start = 2
while start <= length:
    print(start)
    start += 2

#while check method
length = int(input("Please input your number: "))
start = 1
while start <= length:
    if start % 2 == 0:
        print(start)
    start += 1

#range method:
length = int(input("Please input your number: "))
for number in range(2, length + 1, 2):
    print(number)


