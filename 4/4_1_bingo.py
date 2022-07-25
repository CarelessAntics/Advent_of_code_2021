#play bingo against a giant squid
#Q1: win the game
#Q2: lose the game on purpose

import itertools


#Check if bingo number exists on the board
def check_hit(board, n):
    if n in itertools.chain.from_iterable(board): #Flattens nested list
        return True
    else:
        return False

#Get the position of a number on the board
def get_index(board, n):
    for y, d in enumerate(board):
        if n in d:
            x = d.index(n)
            return (x, y)
    return None

#Check the rows and columns on the board and if everything matches on any one of them, return True
def check_win(board_bool):
    cols = list(zip(*board_bool))
    for r in board_bool + cols:
        if all(r):
            return True
    return False

#Flatten the lists for both numbers and hitmarks, and find only the unselected numbers. Returns the sum of these numbers as the score
def get_score(board, marks):
    board_flat = itertools.chain.from_iterable(board)
    marks_flat = list(itertools.chain.from_iterable(marks))
    unselected = [d for i, d in enumerate(board_flat) if not marks_flat[i]]
    return sum(unselected)

#Q1, play the bingo and find the first board that wins. Returns the score multiplied by the winning number as the answer
def win_bingo_Q1(data, numbers):
    marks = [[[False for x in range(5)] for y in range(5)] for z in range(len(data))] #Nested list of booleans in the same structure as the input data to track which numbers are called
    
    for n in numbers:
        for i, board in enumerate(data):
            is_hit = check_hit(board, n)
            if is_hit:
                hit_index = get_index(board, n)
                marks[i][hit_index[1]][hit_index[0]] = True

            if check_win(marks[i]):
                return get_score(board, marks[i]) * n

#Q2, copypasted from Q1 with the exception of added win tracker to find the last board to win
def lose_bingo_Q2(data, numbers):
    marks = [[[False for x in range(5)] for y in range(5)] for z in range(len(data))]
    wins = set()
    
    for n in numbers:
        for i, board in enumerate(data):
            if i in wins:
                continue
            is_hit = check_hit(board, n)
            if is_hit:
                hit_index = get_index(board, n)
                marks[i][hit_index[1]][hit_index[0]] = True

            columns = list(zip(*marks[i]))
            if check_win(marks[i]):
                if len(wins) != len(data)-1:
                    wins.add(i)
                else:
                    return get_score(board, marks[i]) * n

def main():

    with open("4\\puzzle_input.txt", "r") as f:
        raw_data = f.read()
        puzzle_input = raw_data.split('\n')
        bingo_numbers = [int(x) for x in puzzle_input.pop(0).split(',')]

    puzzle_data = []
    helper_list = []
    for i, d in enumerate(puzzle_input[1:]):
        if d != '':
            helper_list.append([int(x) for x in d.split(' ') if x != ''])
        if (d == '') or (i == len(puzzle_input[1:])-1):
            puzzle_data.append(helper_list)
            helper_list = []
            continue

    Q1_answer = win_bingo_Q1(puzzle_data, bingo_numbers)
    Q2_answer = lose_bingo_Q2(puzzle_data, bingo_numbers)

    print(f"Q1 answer is: {Q1_answer}")
    print(f"Q2 answer is: {Q2_answer}")


if __name__ == "__main__":
    main()