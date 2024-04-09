def palin_check(word):
    i = 0
    while i < (len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
        else:
            i += 1
    return True


word = input("Please type thw word you want to determine as a palindrome or not:").lower()
if palin_check(word):
    print("Yes,", word, "is a palindrome")
else:
    print("No,", word, "is not a palindrome")
