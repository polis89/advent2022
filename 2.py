total = 0

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
    'A': 1,
    'B': 2,
    'C': 3
}

with open('2_input.txt', 'r') as f:
    for line in f:
        if len(line) == 4:
            [opponent, me] = str(line).split()
            total = total + scores[me]
            if scores[me] == scores[opponent]:
                total = total + 3
            if (scores[opponent] % 3 + 1) == scores[me]:
                print("======")
                print(scores[opponent])
                print(scores[me])
                total = total + 6


print(total)