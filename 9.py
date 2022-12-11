position_head = [4,0]
position_tail = [4,0]
visited = set()
visited.add(str(position_tail[0]) + "_" + str(position_tail[1]))

with open('9_input.txt', 'r') as f:
    for line in f:
        direction = line.split(" ")[0]
        steps = int(line.split(" ")[1])

        for step in range(0, steps):
            if direction == "R":
                position_head[1] += 1
            elif direction == "L":
                position_head[1] -= 1
            elif direction == "U":
                position_head[0] -= 1
            elif direction == "D":
                position_head[0] += 1
            
            if abs(position_head[0] - position_tail[0]) > 1:
                position_tail[0] = int((position_head[0] + position_tail[0]) / 2)
                if abs(position_head[1] - position_tail[1]) == 1:
                    position_tail[1] = position_head[1]
            if abs(position_head[1] - position_tail[1]) > 1:
                position_tail[1] = int((position_head[1] + position_tail[1]) / 2)
                if abs(position_head[0] - position_tail[0]) == 1:
                    position_tail[0] = position_head[0]
            
            visited.add(str(position_tail[0]) + "_" + str(position_tail[1]))

print(visited)
print(len(visited))
