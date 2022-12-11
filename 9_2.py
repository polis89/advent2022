knot_positions = [[10000,10000] for x in range(0,10)]
visited = set()
visited.add(str(knot_positions[9][0]) + "_" + str(knot_positions[9][1]))

rows = 5
columns = 6
def print_state(knots):
    for row in range(0, rows):
        for col in range(0, columns):
            try:
                index = knot_positions.index([row,col])
                if index == 0:
                    index = 'H'
                print(index, end = '')
            except:
                print('.', end = '')
        print()
    print()

with open('9_input.txt', 'r') as f:
    for line in f:
        direction = line.split(" ")[0]
        steps = int(line.split(" ")[1])

        for step in range(0, steps):
            if direction == "R":
                knot_positions[0][1] += 1
            elif direction == "L":
                knot_positions[0][1] -= 1
            elif direction == "U":
                knot_positions[0][0] -= 1
            elif direction == "D":
                knot_positions[0][0] += 1

            for next_knot in range(1,10):
                if abs(knot_positions[next_knot - 1][0] - knot_positions[next_knot][0]) > 1 and abs(knot_positions[next_knot - 1][1] - knot_positions[next_knot][1]) > 1:
                    knot_positions[next_knot][0] = int((knot_positions[next_knot - 1][0] + knot_positions[next_knot][0]) / 2)
                    knot_positions[next_knot][1] = int((knot_positions[next_knot - 1][1] + knot_positions[next_knot][1]) / 2)
                elif abs(knot_positions[next_knot - 1][0] - knot_positions[next_knot][0]) > 1:
                    knot_positions[next_knot][0] = int((knot_positions[next_knot - 1][0] + knot_positions[next_knot][0]) / 2)
                    if abs(knot_positions[next_knot - 1][1] - knot_positions[next_knot][1]) == 1:
                        knot_positions[next_knot][1] = knot_positions[next_knot - 1][1]
                elif abs(knot_positions[next_knot - 1][1] - knot_positions[next_knot][1]) > 1:
                    knot_positions[next_knot][1] = int((knot_positions[next_knot - 1][1] + knot_positions[next_knot][1]) / 2)
                    if abs(knot_positions[next_knot - 1][0] - knot_positions[next_knot][0]) == 1:
                        knot_positions[next_knot][0] = knot_positions[next_knot - 1][0]
            
            # print_state(knot_positions)
            visited.add(str(knot_positions[9][0]) + "_" + str(knot_positions[9][1]))

print(visited)
print(len(visited))
