def data_reverse(data):
    data2 = []
    lenght = int(len(data)/8)
    b = 0
    x = 0

    while x < lenght:
        i = 0
        tempstring = ""
        while i < 8:
            tempstring += str(data[i + (8*x)])
            i += 1
        data2 = list(tempstring) + data2
        x += 1

    print(tempstring)
    print(data2)

#    for x in / 8:
#        for i in 8:
#            b += data[i]
#        data2 = b + data2
#    return data2


data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
print(data1)
print(data_reverse(data1))