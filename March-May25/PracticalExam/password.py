def is_strong(pw):
    l = False
    u = False
    for c in pw:
        if c.islower():
            l = True
        if not c.islower():
            u  = True
    return len(pw) > 7 and l and u


print(is_strong("abc"))
print(is_strong("abcdefgh"))
print(is_strong("ABCDEFGH"))
print(is_strong("abcHJK"))
print(is_strong("abcDEFhij"))