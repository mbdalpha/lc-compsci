def unique_in_order(sequence):
    if not sequence:
        return []

    final = [sequence[0]]
    for i in sequence:
        if i != final[-1]:
            final.append(i)

    return final

print(unique_in_order("ABBCcA"), ["A", "B", "C", "c", "A"])