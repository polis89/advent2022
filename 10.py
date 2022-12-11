sum = 0
cycle = 0
x = 1
target_cycles = [20, 60, 100, 140, 180, 220]

with open('10_input.txt', 'r') as f:
    for line in f:
        op = line[0:len(line)-1].split(" ")[0]
        if op == "addx":
            arg = int(line[0:len(line)-1].split(" ")[1])
            for step in range(0,2):
                cycle += 1
                # print(f"during {cycle} the value is {x}")
                if cycle in target_cycles:
                    print(f"during {cycle} the value is {x}")
                    sum += cycle * x
            x += arg
            # print(f"x changed to {x} on cycle {cycle}")
        elif op == "noop":
            print("test")
            cycle += 1
            print(f"during {cycle} the value is {x}")
            if cycle in target_cycles:
                print(f"during {cycle} the value is {x}")
                sum += cycle * x

print(sum)
