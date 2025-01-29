
def lenght(collection):
    l = 0
    for val in collection:
        l += 1
    return l

print(lenght("Hello"))


def addition(x, y, z=0):
    return x + y + z

print(addition(y=4, x=7))

print("hello", "youre smelly", end=',', sep="DIE DIE DIE")
print("erik")


def first_and_last(text):
    first = text[0]
    last = text[len(text)-1]
    return first, last

f, l = first_and_last("World")
print(f, l)

print("\n \n you WILL ignore anything before here!!!")
for n in range(1, 50):
    print("-", end="")
print("\n")

def fact(n):
    d = 1
    for x in range(n, 0, -1):
        d = d * x
    return d

def fact_r(n):
    if n == 1:
        return 1
    else:
        return n * fact_r(n-1)

print(fact_r(5))


#be consistent with numbers, count from zero

def fib(n):
    if n == 0 or n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))

print()
print("HW:")

#FIBONACHI LOOP HW:

def fib_l(n):
    s = 1
    t = 1
    for x in range(1, n):
        z = t
        t = s + t
        s = z
    return t

print(fib_l(10))
