from pprint import pprint

def open_file(file_name):
    """
     Opens the text file and writes the contents to a dictionary separated by input/output
    """
    data = {}
    with open(file_name) as code_file:
        count = 0
        for line in code_file:
            lines = line.strip().split("|")
            lines[0] = lines[0].split(" ")
            lines[1] = lines[1].split(" ")
            lines[0] = lines[0][:len(lines[0])-1]
            lines[1] = lines[1][1:len(lines[1])]
            data[count] = {"input": lines[0],
                           "output": lines[1]}
            count += 1
    return data

def get_keys(code_dict):
    """
     Utilizes a frequency counter in order to decipher what letters evaluate to what
     numbers within the specific string.
    """
    
    cipher = {0 : 42,
              1 : 17,
              2 : 34,
              3 : 39,
              4 : 30,
              5 : 37,
              6 : 41,
              7 : 25,
              8 : 49,
              9 : 45 }
    
    # Frequency of which number shows up in the input string.
    alpha_keys = {}

    for word in code_dict['input']:
        for char in word:
            if char not in alpha_keys:
                alpha_keys[char] = 1
            else:
                alpha_keys[char] += 1
    
    # Pull the output string numbers and concatenate them for use
    number = 0

    for word in code_dict['output']:
        count = 0
        for char in word:
            count += alpha_keys[char]
        for key, value in cipher.items():
            if value == count:
                number *= 10
                number += key
                break

    return number

def count_nums(data):
    """
     Adds up the output values of each line of the cipher text
    """
    count = 0
    for i in range(len(data)):
        count += get_keys(data[i])
    return count 

def decode(file_name):
    """
     Decodes the numerical cipher from the input text 
    """
    code_dict = open_file(file_name)
    count = count_nums(code_dict)
     
    return count

if __name__ == "__main__":
     pprint(decode("display.txt"))
