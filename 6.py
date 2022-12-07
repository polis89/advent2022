position = 0
last_four = []

with open('6_input.txt', 'r') as file:
    while True:
        position = position + 1
        char = file.read(1)

        if not char:
            print("cannot find start")
            break

        last_four.append(char)

        if len(last_four) < 4:
            continue

        if len(last_four) > 4:
            last_four.pop(0)

        if len(set(last_four)) == len(last_four):
            break

print(position)
