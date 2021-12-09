from pprint import pprint

def open_file(file_name):
    """
     Opens a text file and creates a N * M list of heights
    """ 
    heights = []   
    with open(file_name) as h:
        for line in h:
            line = line.strip()
            line = list(map(int, line))
            heights.append(line)

    return heights

def build_basins(heights):
    """
     Builds a list of basins areas of the height map that are less than
     9 and connected.
    """
    basins = []

    N = len(heights)
    M = len(heights[0])
    
    for i in range(N):
        for j in range(M):
            if heights[i][j] != 9 and heights[i][j] != 'X':
                total, heights = check_basin(heights, i, j)
                basins.append(total)
    return basins

def check_basin(heights, i, j):
    """
     Uses Breadth First Search to analyze the width of a given basin
     from a input starting point.
    """
    stack = [(i,j)]

    total = 1
    heights[i][j] = 'X'

    while len(stack) > 0:
        x,y = stack.pop(0)
        if x - 1 >= 0:
            if heights[x-1][y] != 'X' and heights[x-1][y] < 9:
                total += 1
                stack.append((x-1, y))
                heights[x-1][y] = 'X'
        if x + 1 < len(heights):
            if heights[x+1][y] != 'X' and heights[x+1][y] < 9:
                total += 1
                stack.append((x+1, y))
                heights[x+1][y] = 'X'
        if y - 1 >= 0:
            if heights[x][y-1] != 'X' and heights[x][y-1] < 9:
                total += 1
                stack.append((x, y-1))
                heights[x][y-1] = 'X'
        if y + 1 < len(heights[0]):        
            if heights[x][y+1] != 'X' and heights[x][y+1] < 9:
                total += 1
                stack.append((x, y+1))
                heights[x][y+1] = 'X'
    return total, heights 

def count_heights(heights):
    """
     Counts the heights of the lowest points in the height map.
    """
    count = 0

    N = len(heights)
    M = len(heights[0])

    for i in range(N):
        for j in range(M):
            top = check_top(heights, i, j)
            left = check_left(heights, i, j)
            right = check_right(heights, i, j)
            bottom = check_bottom(heights, i, j)
            if top and left and right and bottom:
                count += 1 + heights[i][j] 

    return count

def check_top(heights, i, j):
    """
     Verifies whether the top number is greater than the current number.
    """
    if i - 1 >= 0:
        if heights[i][j] >= heights[i-1][j]:
           return False

    return True

def check_left(heights, i, j):
    """
     Verifies whether the left number is greater than the current number
    """
    if j - 1 >= 0:
        if heights[i][j] >= heights[i][j-1]:
            return False

    return True

def check_right(heights, i, j):
    """
     Verifies whether the right number is greater than the current number
    """
    if j + 1 < len(heigths[0]):
        if heights[i][j] >= heights[i][j+1]:
            return False

    return True

def check_bottom(heights, i, j):
    """
     Verifies whether the bottom number is greater than the current number
    """
    if i + 1 < len(heights):
        if heights[i][j] >= heights[i+1][j]:
            return False

    return True

def calculate_tops(basins):
    """
     Calculates the product of the top three largest basins widths.
    """
    one = max(basins)
    basins.remove(max(basins))
    two = max(basins)
    basins.remove(max(basins))
    three = max(basins)
    basins.remove(max(basins))
   
    return one * two * three
 
def height_map(file_name):
    """
     builds up the height map from a text file and calculates the basins
     and the lowest points.
    """
    heights = open_file(file_name)
    count = count_heights(heights)   
    basins = build_basins(heights)
    top_heights = calculate_tops(basins)

    return top_heights

if __name__ == "__main__":
    #print(height_map("debug.txt"))
    print(height_map("heights.txt"))
