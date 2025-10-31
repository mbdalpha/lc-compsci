def factorial_lp(x):
    ans = 1
    for i in range(1, x + 1):
        ans = ans * i
    return ans

print(factorial_lp(3), factorial_lp(5))

def factorial_rc(x):
    if x != 1:
        return x * factorial_rc(x-1)
    else:
        return 1

print(factorial_rc(3), factorial_rc(5))

def sum_lp(lst):
    total = 0
    for i in lst:
        total += i
    return total

print(sum_lp([1,2,3]))

def sum_rc(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_rc(lst[1:])

print(sum_rc([1,2,3,4]))
