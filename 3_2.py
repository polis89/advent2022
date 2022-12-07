
sum_priority = 0

def get_priority(c):
    ascii = ord(c)
    if ascii > 90:
        return ascii - 96
    else:
        return ascii - (64-26)


with open('3_input.txt', 'r') as f:
    while True:
        line_1 = f.readline()
        if not line_1:
            break
        line_2 = f.readline()
        line_3 = f.readline()
        types_in_1 = set()
        types_in_2 = set()
        for symb_1 in line_1:
            types_in_1.add(symb_1)
        for symb_2 in line_2:
            if symb_2 in types_in_1:
                types_in_2.add(symb_2)
        for symb_3 in line_3:
            if symb_3 in types_in_2:
                sum_priority = sum_priority + get_priority(symb_3)
                break

print(sum_priority)