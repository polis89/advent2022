total = 0

scores = {
    'A': 1,
    'B': 2,
    'C': 3
}

win = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

with open('2_input.txt', 'r') as f:
    for line in f:
        if len(line) == 4:
            [opponent, result] = str(line).split()
            if result == 'Y':
                me = opponent
                total = total + 3 + scores[me]
            if result == 'Z':
                me = win[opponent]
                total = total + 6 + scores[me]
            if result == 'X':
                me = lose[opponent]
                total = total + scores[me]

print(total)