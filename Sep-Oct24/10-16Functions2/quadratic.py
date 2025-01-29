import math

def quadratic(a, b, c):
    if b**2 - 4*a*c < 0:
        print("The quadratic has complex numbers")
        return math.nan, math.nan

    det = math.sqrt(b**2 - 4*a*c)
    a1 = (-b + det) / (2 * a)
    a2 = (-b - det) / (2 * a)
    return a1, a2

ans1, ans2 = quadratic(3, 5, -2)
print(f"x = {ans1} and {ans2}.")