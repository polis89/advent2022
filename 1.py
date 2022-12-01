
max_cal = 0
cur_cal = 0

with open('1_input.txt', 'r') as f:
    for line in f:
        if len(line) == 1:
            max_cal = max(cur_cal, max_cal)
            cur_cal = 0
        else:
            cur_cal += int(line)

print(max_cal)