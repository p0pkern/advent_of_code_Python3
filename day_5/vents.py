from pprint import pprint

def vent_file(file_name):
    """

    """
    vent_dict = {}
    with open(file_name) as v_file:
        counter = 0
        for line in v_file:

            nums = line.strip().split('->')
            nums = [x.strip().split(",") for x in nums] 
           
            vent_dict[counter] = nums
            counter += 1 
    return vent_dict

def vent_count(vent_dict):
    """
    """
    grid = {}
    for key, value in vent_dict.items():
        x,y = value[0]
        x2,y2 = value[1]
        
        x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
        
        if x == x2:
           if y < y2:
              for i in range(y, y2 + 1):
                  index = str(x)+","+str(i)
                  if index not in grid:
                      grid[index] = 1
                  else:
                      grid[index] += 1
           elif y > y2:
              for i in range(y2, y + 1):
                  index = str(x)+","+str(i)
                  if index not in grid:
                      grid[index] = 1
                  else:
                      grid[index] += 1
        elif y == y2:
            if x > x2:
               for i in range(x2, x + 1):  
                  index = str(i)+","+str(y)
                  if index not in grid:
                      grid[index] = 1
                  else:
                      grid[index] += 1
            elif x < x2:
               for i in range(x, x2 + 1):
                  index = str(i)+","+str(y)
                  if index not in grid:
                      grid[index] = 1
                  else:
                      grid[index] += 1
        
        else:
            index = x
            index2 = y
            
            if x < x2:
                if y < y2:
                    while index < x2 or y < y2:
                        grid_value = str(index)+","+str(index2)
                        if grid_value not in grid:
                           grid[grid_value] = 1
                        else:
                           grid[grid_value] += 1

                        if index <= x2:
                            index += 1
                        if index2 <= y2:
                            index2 += 1
                elif y > y2:
                    while index < x2 or y > y2:
                        grid_value = str(index)+","+str(index2)
                        if grid_value not in grid:
                           grid[grid_value] = 1
                        else:
                           grid[grid_value] += 1

                        if index <= x2:
                            index += 1
                        if index2 >= y2:
                            index2 -= 1
            elif x > x2:
                 
               if y < y2:
                    while index > x2 or y < y2:
                        grid_value = str(index)+","+str(index2)
                        if grid_value not in grid:
                           grid[grid_value] = 1
                        else:
                           grid[grid_value] += 1

                        if index >= x2:
                            index -= 1
                        if index2 <= y2:
                            index2 += 1
               elif y > y2:
                     while index > x2 or y > y2:
                        grid_value = str(index)+","+str(index2)
                        if grid_value not in grid:
                           grid[grid_value] = 1
                        else:
                           grid[grid_value] += 1

                        if index >= x2:
                            index -= 1
                        if index2 >= y2:
                            index2 -= 1
    return grid

def total(grid):
    """

    """
    count = 0
    for key, value in grid.items():
        if value > 1:
            count += 1

    return count

def vent_number(file_name):
    """

    """
    vent_dict = vent_file(file_name)
    count = vent_count(vent_dict)
    totals = total(count)
    
    return totals

if __name__ == "__main__":
   # print(vent_number("vent_data.txt"))
    print(vent_number("debug.txt"))    
