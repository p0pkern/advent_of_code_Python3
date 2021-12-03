from power_consumption import get_lines, get_gamma, get_epsilon
from pprint import pprint

def line_count(lines, index):
    zeros =  ones = 0

    for i in range(len(lines)):
        if lines[i][index] == "0":
            zeros += 1
        else:
            ones += 1            
    
    return zeros, ones

def oxygen_rating(lines):
    """
    Filters out the list of binary numbers to find the oxygen rating.
    The oxygen rating is the single binary number most similar to the
    gamma rating (All bits are the most common between all binary nums)
    """
    
    index = 0    
    while index < 12:
        if len(lines) <= 2:
            if len(lines) == 1:
                return lines[0]
            if lines[0][index] == "1":
                return lines[0]
            else:
                return lines[1]

        else:
           lines =  filter_oxygen(lines, index)    
        index += 1
    return lines 

def filter_oxygen(line_list, index):
    """
    
    """
    zeros, ones = line_count(line_list, index)
    
    out_list = []
    for line in line_list:
        if zeros > ones:
            if line[index] == "0":
                out_list.append(line)
        elif ones >= zeros:
            if line[index] == "1":
                out_list.append(line)
        else:
            out_list.append(line)
    return out_list
   
def CO2_rating(lines):
    """
    Filters out the list of binary numbers to find the Co2 rating.
    The Co2 rating is the single binary number most similar to the
    epsilon rating (All bits are the least common bits among all
    binary numbers.)
    """

    index = 0    
    while index < 12:
        if len(lines) <= 2:
            if len(lines) == 1:
                return lines[0]
            if lines[0][index] == "0":
                return lines[0]
            else:
                return lines[1]

        else:
           lines =  filter_CO2(lines, index)    
        index += 1
    return lines 


def filter_CO2(line_list, index):
   """
   """

   zeros, ones = line_count(line_list, index)

         
   out_list = []
   for line in line_list:
       if zeros <= ones:
            if line[index] == "0":
               out_list.append(line)
       elif ones < zeros:
           if line[index] == "1":
               out_list.append(line)
       else:
           out_list.append(line)
   return out_list


def life_support_rating(file_name):
    """
    Calculates the life support rating which is the oxygen rating
    multiplied by the CO2 rating.
    """
    lines = get_lines(file_name)
    oxygen = oxygen_rating(lines)
    CO2 = CO2_rating(lines)
    total = int(oxygen, 2) * int(CO2, 2)
    return oxygen, CO2, total

if __name__ == "__main__":
   pprint(life_support_rating("binary.txt"))
