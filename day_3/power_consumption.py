"""
Name: Chris Peterman
Title: Gamma, Epsilon Calculator
Description: This is code for solving the day 3 equation for the Advent of Code 2021
"""


def get_lines(file_name):
    """
     Opens the file and saves the lines of the file in a list
     to return to a file reading program.
    """
    lines = None

    with open(file_name) as binary_file:
        lines = binary_file.readlines()

    return lines


def get_gamma(binary_list):
    """
     Receives a list of binary numbers. It will compare the amount of
     ones and zeros in each bit spot of all binary numbers and then 
     create a new binary number of the most common bits.
     For example:
        1100
        1001
        0011
        
        The gamma would be 1001 since 1 is the most common of the MSB
        followed by 0, followed by 0, and finally the LSB most common
        is 1.
    """

    gamma_dict = {}
    for line in binary_list:
        for k in range(len(line)):
            if k not in gamma_dict:
                if line[k] == "0":
                    gamma_dict[k] = [1,0]
                elif line[k] == "1":
                    gamma_dict[k] = [0,1]
            else:
                if line[k] == "0":
                    gamma_dict[k][0] += 1
                elif line[k] == "1":
                    gamma_dict[k][1] += 1

    return gamma_dict

def out_gamma(gamma_dict):

    out_gamma = ""
    for j in range(len(gamma_dict)):
        if gamma_dict[j][0] > gamma_dict[j][1]:
            out_gamma += "0"
      
        else:
            out_gamma += "1"

    return out_gamma


def get_epsilon(gamma):
    """
     Receives the binary gamma number and flips the bits
     in order to get the epsilon binary number. Epsilon
     represents the least common bits in each row.
    """
    out_epsilon = ""
    for i in range(len(gamma)):
        if gamma[i] == "0":
            out_epsilon += "1"
        elif gamma[i] == "1":
            out_epsilon += "0"

    return out_epsilon


def power_consumption(file_name):
    """
     Calculates the power consumption of a submarine. Which is 
     the Gamma multiplied by the Epsilon values.
    """                

    lines = get_lines(file_name)
    gamma_dict = get_gamma(lines)
    gamma = out_gamma(gamma_dict)
    epsilon = get_epsilon(gamma)
    power_consumption = int(gamma, 2) * int(epsilon, 2)

    return power_consumption


if __name__ == "__main__":
    total = power_consumption("binary.txt")
    print(total)
