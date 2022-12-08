matrix = []
count = 0

with open('8_input.txt', 'r') as f:
    for line in f:
        matrix.append([int(s) for s in line[0:len(line)-1]]);

    for row_index in range(1,len(matrix) - 1):
        row = matrix[row_index]
        suspected_column_indexes_left = set()
        max_left = -1
        for column_index in range(len(row)):
            if max_left >= row[column_index]:
                suspected_column_indexes_left.add(column_index)
            else:
                max_left = row[column_index]
        max_right = -1
        suspected_column_indexes = set()
        for column_index in range(len(row) - 1, 0, -1):
            if max_right >= row[column_index] and column_index in suspected_column_indexes_left:
                suspected_column_indexes.add(column_index)
            else:
                max_right = row[column_index]
        print(f"for row {row} suspected indexes: {suspected_column_indexes}")

        for suspected_column_index in suspected_column_indexes:
            is_hidden = False
            for row_index_check in range(row_index - 1, -1, -1):
                if matrix[row_index][suspected_column_index] <= matrix[row_index_check][suspected_column_index]:
                    is_hidden = True
                    break
            if not is_hidden:
                continue
            is_hidden = False
            for row_index_check in range(row_index + 1, len(matrix)):
                if matrix[row_index][suspected_column_index] <= matrix[row_index_check][suspected_column_index]:
                    is_hidden = True
                    break
            if is_hidden:
                print(f"found hidden tree on [{row_index, suspected_column_index}]")
                count += 1

total_trees = len(matrix) * len(matrix[0])
print(total_trees - count)