
sum_priority = 0
count = 0
count_err = 0

def get_priority(c):
    ascii = ord(c)
    if ascii > 90:
        return ascii - 96
    else:
        return ascii - (64-26)


with open('3_input.txt', 'r') as f:
    for line in f:
        flag = False
        count = count + 1
        types_in_1 = set()
        items = str(line)
        comp_size = len(line) // 2
        for symb_1 in items[0:comp_size]:
            types_in_1.add(symb_1)
        for symb_2 in items[comp_size:]:
            if symb_2 in types_in_1:
                count_err = count_err + 1
                flag = True
                sum_priority = sum_priority + get_priority(symb_2)
                break

print(sum_priority)