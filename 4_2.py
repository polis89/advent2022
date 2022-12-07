count = 0


with open('4_input.txt', 'r') as f:
    for line in f:
        line_data = line[0:len(line)-1].split(",")
        [first_start, first_end] = map(lambda x: int(x), line_data[0].split("-"))
        [second_start, second_end] = map(lambda x: int(x), line_data[1].split("-"))
        if first_start<=second_start and first_end >=second_start:
            count = count + 1
            print(f"====\n{first_start} - {first_end}")
            print(f"{second_start} - {second_end}")
        elif first_start>=second_start and first_start<=second_end:
            count = count + 1
            print(f"====\n{first_start} - {first_end}")
            print(f"{second_start} - {second_end}")
        

print(count)