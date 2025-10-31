from plotly.express import strip

a = [5, 7, 2, 4, 10]
t = "Hello"
b="hsjahdkhksdhakjshdsd"

print(a[1:4])
print(t[2:5])

print(b[::-1])


def remove_first_last(t):
    return t[1:-1]

print(remove_first_last("example") == "xampl")
print(remove_first_last("a") == "")
print(remove_first_last("") == "")

def middle(t):
    i = len(t)
    if i%2 != 0:
        return t[i//2:-(i//2)]
    else:
        return t[(i//2) - 1:-(i//2) + 1]


print(middle("abcde") == "c")
print(middle("abcd") == "bc")

def rotate(t, a):
    return  t[(a+1):] + t[:(a+1)]

print(rotate("abcdefg", 3))
print(rotate("abcdefg", 3) == "efgabcd")


def count_alpha(t):
    o = []
    for i in t:
        if i.isalnum():
            o.append(i)
    return len(o)


print(count_alpha("No punctuation here") == 17)
print(count_alpha("Hello, World!") == 10)

def count_vowels(t):
    o = []
    v = ["a", "e", "i", "o", "u"]
    for i in t:
        if v.count(i.lower()) :
            o.append(i)
    return len(o)

print(count_vowels("Programming") == 3)


def split_by(txt, chr):
    ary = []
    split_point = 0
    while txt.find(chr) != -1:
        split_point = txt.find(chr)
        ary.append(txt[0:split_point])
        txt = txt[split_point + 1:]

    ary.append(txt)

    return ary

print(split_by("apple,banana,cherry", ","))
print(split_by("A-b-c-d", "-"))

def reverse_words(txt):
    split = txt.split(" ")
    rev = " "
    for i in split:
        rev = i + " " + rev
    return rev.strip()

print(reverse_words("The quick brown fox"))

def cap_sen(txt):
    split = txt.split(" ")
    cap = " "
    for i in split:
        cap += (i.capitalize() + " ")
    return cap.strip()

print(cap_sen("this is a sentence"))


word1 = "Silent"
word2 = "listen"

print(sorted(word1.lower()) == sorted(word2.lower()))