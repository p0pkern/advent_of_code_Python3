def open_file(file_name):
    """
     Opens the file and calculates the score from corrupted lines, and then
     returns that score along with a list of incomplete lines for processing
    """ 
    total = 0
    
    incomplete = []
    with open(file_name) as s:
    
        for line in s:
            line = line.strip()
            stack = []
            
            score = 0
            for char in line:
                if char in ['[','(','{','<']:
                    stack.append(char)

                else:
                    value = stack.pop()
                    if char == "]":
                        if value != "[":
                            score += 57
                            break
                    elif char == ")":
                        if value != "(":
                            score += 3
                            break
                    elif char == "}":
                        if value != "{":
                            score += 1197
                            break
                    elif char == ">":
                        if value != "<":
                            score += 25137
                            break
            total += score
            if score == 0 and len(stack) > 1:
                incomplete.append(line)                

    return incomplete, total

def total_incompletes(incomplete):
    """
     Totals the score of incompletes and returns the value.
    """
    totals = []
    for string in incomplete:
        stack = []
        for char in string:
            if char in ['[','(','{','<']:
                stack.append(char)
            else:
                stack.pop()
        score = 0
        while len(stack) > 0:
            value = stack.pop()
            
            if value == "(":
                score *= 5
                score += 1
            elif value == "[":
                score *= 5
                score += 2
            elif value == "{":
                score *= 5
                score += 3
            elif value == "<":
                score *= 5
                score += 4
        totals.append(score)
     
    totals.sort()
    return totals[len(totals) // 2]

def syntax_score(file_name):
    """
     Finds the score of the corrupted lines and the incomplete lines
    """
 
    incomplete, total = open_file(file_name)
    score_incomplete = total_incompletes(incomplete)
    
    return total, score_incomplete


if __name__ == "__main__":
    print(syntax_score("debug.txt"))
    print(syntax_score("console.txt"))
