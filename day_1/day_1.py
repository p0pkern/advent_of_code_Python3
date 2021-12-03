with open('input.txt') as file_name:
    lines = file_name.readlines()

    count = 0
    for i in range(2,  len(lines)):
        window_1 = int(lines[i-3]) + int(lines[i-2]) + int(lines[i-1])
        window_2 = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
        if window_1 < window_2:  
            count += 1

print(count)
