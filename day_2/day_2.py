with open('depth.txt') as file_name:
    lines = file_name.readlines()
    
    horizontal = 0
    depth = 0
    aim = 0
  
    for line in lines:
        split_lines = line.split(" ")
        direction = split_lines[0]
        amount =  int(split_lines[1])
        if direction == 'forward':
            horizontal += amount
            depth += amount * aim
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount

print(horizontal * depth) 
