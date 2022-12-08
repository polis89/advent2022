matrix = []
max_view = 0

with open('8_input.txt', 'r') as f:
    for line in f:
        matrix.append([int(s) for s in line[0:len(line)-1]])

    for row_index in range(1, len(matrix) - 1):
        for col_index in range(1, len(matrix[0]) - 1):
            tree_height = matrix[row_index][col_index]
            view_score = 0
            visible_left = 0
            for check_col in range(col_index - 1, -1, -1):
                visible_left += 1
                if matrix[row_index][check_col] >= matrix[row_index][col_index]:
                    break
            view_score = visible_left
            visible_right = 0
            for check_col in range(col_index + 1, len(matrix[0])):
                visible_right += 1
                if matrix[row_index][check_col] >= matrix[row_index][col_index]:
                    break
            view_score *= visible_right
            visible_up = 0
            for check_row in range(row_index - 1, -1, -1):
                visible_up += 1
                if matrix[check_row][col_index] >= matrix[row_index][col_index]:
                    break
            view_score *= visible_up
            visible_down = 0
            for check_row in range(row_index + 1, len(matrix)):
                visible_down += 1
                if matrix[check_row][col_index] >= matrix[row_index][col_index]:
                    break
            view_score *= visible_down
            if view_score > max_view:
                max_view = view_score
                # print(f"max_view {row_index} {col_index}")
                # print(f"visible_left {visible_left}")
                # print(f"visible_right {visible_right}")
                # print(f"visible_up {visible_up}")
                # print(f"visible_down {visible_down}")

print(max_view)

    
