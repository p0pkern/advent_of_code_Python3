from pprint import pprint

def vent_file(file_name):
    """
     Opens and reads a text file with plot points as
     x,y -> x2, y2 and assigns them to a dictionary
     for processing.
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
     Populates a dictionary with values from a plot for points
     a to b in a dictionary. If they show up they are marked with
     the integer 1. If they show up again the integer is incremented.
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
           if abs(y2 - y) < abs(x2 - x):
              if x > x2:
                 grid =  plotLineLow(x, y, x2, y2, grid)
                 grid =  plotLineLow(x2, y2, x, y, grid)
              else:
                 grid =  plotLineLow(x, y, x2, y2, grid)
                 grid =  plotLineLow(x2, y2, x, y, grid)
           else:
              if y > y2:
                 grid =  plotLineHigh(x, y, x2, y2, grid)
                 grid =  plotLineHigh(x2, y2, x, y, grid)
              else:
                 grid = plotLineHigh(x, y, x2, y2, grid)
                 grid = plotLineHigh(x2, y2, x, y, grid) 

                  
    return grid

def plotLineLow(x0, y0, x1, y1, grid):
    """
     Plots a diagonal series of points for a 45 degree angle
     using Bresenhams line algorithm from a low point to a high
     point
    """
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy

    D = (2 * dy) - dx
    y = y0

    for x in range(x0, x1 + 1):
         index = str(x)+","+str(y)
         if index not in grid:
             grid[index] = 1
         else:
             grid[index] += 1

         if D > 0:
             y = y + yi
             D = D - (2 * (dy - dx))
         D = D + 2*dy
    
    return grid

def plotLineHigh(x0, y0, x1, y1, grid):
   """
    Plots a diagonal series of points for a 45 degree angle
    using Bresenhams line algorithm. From a high to low point.
   """
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = (2 * dx) - dy
    x = x0

    for y in range(y0, y1 + 1):
        index = str(x)+","+str(y)
        if index not in grid:
           grid[index] = 1
        else:
           grid[index] += 1

        if D > 0:
           x = x + xi
           D = D + (2 * (dx - dy))
        else:
           D = D + 2 * dx

    return grid



def total(grid):
    """
    Totals the amount of grid points > 2
    """
    count = 0
    for key, value in grid.items():
        if value > 1:
            count += 1

    return count

def vent_number(file_name):
    """
    Find the number of vents that intersect from a text file of data
    """
    vent_dict = vent_file(file_name)
    count = vent_count(vent_dict)
    totals = total(count)
    
    return totals

if __name__ == "__main__":
    print(vent_number("vent_data.txt"))
   # print(vent_number("debug.txt"))    
