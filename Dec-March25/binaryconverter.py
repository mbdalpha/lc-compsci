
def from_bin(input):
    x = len(input)
    power = pow(2, x-1)
    total = 0
    for i in input:
        total += int(i) * power
        power = power / 2
    return total
    
print(from_bin("111100101"))


def to_bin(input):
    num_digits = math.ceil(math.log2(value))
    bit_value = 2 ** (num_digits - 1)
    answer = ""
    for _ in range (0, num_digits):
        if value >= bit_value:
            answer -=bit_value
        else:
            answer += "0"
            
        bit_value //=2
    return answer
