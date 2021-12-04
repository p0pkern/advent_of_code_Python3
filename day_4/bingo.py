
def get_data(file_name):
    """
     Pulls from a text file a list of called bingo numbers
     and a list of boards.
    """
    boards = {}
    numbers = []

    with open(file_name) as board_file:
        count = 0
        board_number = 0
        for line in board_file:        
            if count == 0:
                numbers = line.strip()
                numbers = numbers.split(",")
            elif count > 0:
                if line != "\n":
                    row = line.strip()
                    row = row.split()
                    boards[board_number] += [row]
                else:
                    board_number += 1
                    boards[board_number] = []
            count += 1

    return boards, numbers

def check_winner(board):
    """
     Verifies if a board is a winning board due to the following conditions
     a row is empty (we popped every selected value from that row.)
     or that the length of the columns is 4. (we popped one from each row).
    """
    columns = {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0
          } 

    for row in range(len(board)):
        row_x = 0
        for col in range(len(board)):
            if board[row][col] == 'X':
                if row_x == 5:
                   return True
                columns[col] += 1
                row_x += 1

        if row_x == 5:
            return True

    for key, item in columns.items():
        if columns[key] >= 5:
            return True

    return False


def check_score(boards, numbers):
    """
    Removes the matching value from each board row.
    """
    for number in numbers:
        for board_number, board in boards.items():
            for row in range(len(board)):
                if number in boards[board_number][row]:
                    boards[board_number][row] = ['X' if x==number else x for x in boards[board_number][row]]
                winner = check_winner(boards[board_number])
                if winner:
                   if len(boards) == 1:
                       return number, boards[board_number]
                   else:
                       del boards[board_number]
                       return check_score(boards, numbers) 

def calculate_score(winner, number):
    """
     Calculates the score of the bingo game which is the sum of the 
     remaining not tagged numbers multiplied by the last winning number.
    """
    total = 0

    for row in range(len(winner)):
        for col in range(len(winner[row])):
            if winner[row][col] != 'X':
                total += int(winner[row][col])

    return total *  int(number)         

def score(file_name):
   """
    Retrieves the score of the winning bingo game. 
   """
   boards, numbers = get_data(file_name)
   number, winner = check_score(boards, numbers)
   calculation = calculate_score(winner, number)

   return number, calculation


if __name__ == "__main__":
    pprint(score("board_data.txt"))
