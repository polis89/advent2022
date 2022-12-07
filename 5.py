count = 0

with open('5_input.txt', 'r') as f:
    stacks = [[]]
    while True:
        line = f.readline()
        if line.strip().split(" ")[0].isdigit():
            break
        stack_index = 0
        while len(line) - 1 > stack_index * 4 + 1:
            item = line[stack_index * 4 + 1]
            if len(stacks) <= stack_index + 1:
                stacks.append([])
            if item == ' ':
                stack_index = stack_index + 1
                continue
            stacks[stack_index + 1].append(item)
            stack_index = stack_index + 1
        
    line = f.readline()

    count = 3

    while True:
        line = f.readline()
        if not line:
            break
        input_line = line.split(" ")
        amount = int(input_line[1])
        source_stack = int(input_line[3])
        target_stack = int(input_line[5])
        for x in range(amount):
            el = stacks[source_stack].pop(0)
            stacks[target_stack].insert(x, el)

print(stacks)