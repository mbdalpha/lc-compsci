
word_freqs = {}

f = open("ireland.txt", "r")

for line in f:
    words = line.split(" ")
    for word in words:
        word = word.lower()
        if word not in word_freqs:
            word_freqs[word] = 1
        else:
            word_freqs[word] += 1



print(word_freqs)