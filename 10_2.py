cycle = 0
x = 1
result = []

with open('10_input.txt', 'r') as f:
    for line in f:
        op = line[0:len(line)-1].split(" ")[0]
        if op == "addx":
            arg = int(line[0:len(line)-1].split(" ")[1])
            for step in range(0,2):
                if cycle in range(x - 1, x + 2):
                    result.append('#')
                else:
                    result.append('.')
                cycle += 1
                cycle = cycle % 40
                # print(f"during {cycle} the value is {x}")

            x += arg
            # print(f"x changed to {x} on cycle {cycle}")
        elif op == "noop":
            if cycle in range(x - 1, x + 2):
                result.append('#')
            else:
                result.append('.')
            cycle += 1
            cycle = cycle % 40

for x in range(0, len(result)):
    if x % 40 == 0:
        print()
    print(result[x], end='')

print()
