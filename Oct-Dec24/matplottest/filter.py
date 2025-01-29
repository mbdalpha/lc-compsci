
txt_numbers = ["123", "Two", "", "797"]

int_numbers = []
for num in txt_numbers:
    if num.isdigit():
        int_numbers.append(int(num))

print(int_numbers)

int_numbers2 = [int(val) for val in txt_numbers if val.isdigit()]
print(int_numbers2)


uppers = [name.upper() for name in ["Eoin", "Bob", "Ann"] if len(name) == 3]
print(uppers)