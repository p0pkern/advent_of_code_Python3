def open_file(file_name):
    """
     Opens the file and gets all crab positions into a list.
    """
    with open(file_name) as crabs_file:
        lines = crabs_file.readlines()
        lines = lines[0].strip().split(",")
        lines = [int(x) for x in lines]
        return lines

def calculate_fuel(crab_list):
    """
     Calculates the minimum amount of fuel needed to get all crabs
     in the same position.
    """
    minimum = min(crab_list)
    maximum = max(crab_list) + 1
    
    min_fuel = float("inf")

    for i in range(minimum, maximum):
        values = [find_sequence(i, x) for x in crab_list]
        min_fuel = min(min_fuel, sum(values))
    return min_fuel

def find_sequence(start, end):
    """
     Finds the sequence of steps between start and end.
     Example:
         from 1 to 5
         from 1 to 2 = 1 step
         from 1 to 3 = 2 steps
         from 1 to 4 = 3 steps
         from 1 to 5 = 4 steps
         total steps 10
    """
    value = 0
    
    if start > end:
        start, end = end, start
    step = 1

    for i in range(start+1, end + 1):

        value += step
        step += 1
    
    return value
    
def crab_fuel(file_name):
    """
    Calculates the amount of fuel needed for the crabs to move horizontally
    and gives the minimum amount of fuel needed to keep the crabs in sequence.
    """
    crab_list = open_file(file_name)
    fuel = calculate_fuel(crab_list)
    
    return fuel


if __name__ == "__main__":
    print(crab_fuel("debug.txt"))
    print(crab_fuel("crabs.txt"))
