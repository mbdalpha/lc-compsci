def fibonachi_rc(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fibonachi_rc(x-1) + fibonachi_rc(x-2)

print(fibonachi_rc(7), fibonachi_rc(7))

def fibonachi_lp(x):
    a = 0
    if x > 2:
        b = 1
    else:
        b = 0
    while x > 1:
        x -= 1
        p = a + b
        a = b
        b = p
    return b

print(fibonachi_lp(5), fibonachi_lp(7))
