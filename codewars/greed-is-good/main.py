def oneorfive(dice, n, overthree, points):
    points += (dice.count(n) - (3 * overthree)) * n * 10
    if n == 1:
        points = points * 10

    return points


def score(dice):
    numbers = [1, 2, 3, 4, 5, 6]
    points = 0
    for n in numbers:
        overthree = 0
        if dice.count(n) >= 3:
            points += n * 100
            overthree = 1
            if n == 1 or n == 5:
                points = oneorfive(dice, n, overthree, points)
        elif n == 1 or n == 5:
            points = oneorfive(dice, n, overthree, points)

    return points


print(score([5, 5, 5, 5, 6]),  "550")
print(score([1, 1, 1, 3, 1]), "1100")
print(score([2, 3, 4, 6, 2]),    "0")
print(score([4, 4, 4, 3, 3]),  "400")
print(score([2, 4, 4, 5, 4]),  "450")
