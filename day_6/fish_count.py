def open_file(file_name):
    """
     Open fish data file and create a list of fish ages
    """ 
    with open(file_name) as fish_data:
       lines = fish_data.readlines()
       lines = lines[0].strip().split(",")
       lines = [int(x) for x in lines]

       return lines

def cycle_fish(fish, days):
    """
    Cycles by the number of days and updates the fish dictionary to reflect
    the population growth. 
    """
    fish_dict = {}
    for i in range(9):
        fish_dict[i] = 0
   
    for j in fish:
        fish_dict[j] += 1
    
    for _ in range(days):
       fish_dict = cycle_day_dict(fish_dict)

    return fish_dict


def cycle_day_dict(fish_dict):
    """
     Updates the values of the fish dictionary to reflect growth of the
     population of fish.
     All values of 8 will update with the values of 0 to reflect new fish
     born.
     All values of 6 will update with the values of 7 and the birth cycle
     of the mother fish.
     All other values will decrement by 1
    """
    temp = fish_dict[8]
    temp2 = fish_dict[7]
    fish_dict[7] = temp
    temp = fish_dict[6]
    fish_dict[6] = temp2 + fish_dict[0]
    temp2 = fish_dict[5]
    fish_dict[5] = temp
    temp = fish_dict[4]
    fish_dict[4] = temp2
    temp2 = fish_dict[3]
    fish_dict[3] = temp
    temp = fish_dict[2]
    fish_dict[2] = temp2
    temp2 = fish_dict[1]
    fish_dict[1] = temp
    temp = fish_dict[0]
    fish_dict[0] = temp2
    fish_dict[8] = temp
 
    return fish_dict

def total(fish_dict):
    """
     Totals the values of the keys in the fish population dictionary.
    """
    total = 0
    for i in range(len(fish_dict)):
        total += fish_dict[i]

    return total
    
def count_fish(file_name):
    """
     Counts the number of fish that will be populated after a given number
     of days.
    """
    days = 256
    fish = open_file(file_name)
    count = cycle_fish(fish, days)
    value = total(count)

    return value

if __name__ == "__main__":
     print(count_fish("debug.txt"))
     print(count_fish("fish.txt"))
