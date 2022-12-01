from functools import reduce

max_cal = [0, 0, 0]
cur_cal = 0

with open('1_input.txt', 'r') as f:
    for line in f:
        if len(line) == 1:
            for i, c in enumerate(max_cal):
                if cur_cal > c:
                    max_cal.insert(i, cur_cal)
                    max_cal = max_cal[0:3]
                    break
            cur_cal = 0
        else:
            cur_cal += int(line)

sum = reduce(lambda a, b: a + b, max_cal)
print(sum)
