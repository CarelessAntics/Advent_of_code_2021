#AOC13: Fold transparent instructions to reveal messages
#Q1: Count visible dots after 1 fold
#Q2: Complete folding and print out the message

import pprint
import time

START_TIME = time.time()


#Get array size from input coords
def get_array_size(coords):
    w = max(x[0] for x in coords)
    h = max(y[1] for y in coords)
    return (w, h)

#Make a 2D list array filled with dots. Add marks to input coords if any exist
def build_array(coords, w, h):
    point_array = [['.' for x in range(w+1)] for y in range(h+1)]
    if coords is not None:
        for coord in coords:
            point_array[coord[1]][coord[0]] = '#'
        
    return point_array

#Reverses an array along one axis
def flip_array(array, axis):
    if axis == 'y':
        return [row for row in array[::-1]]
    elif axis == 'x':
        return [[x for x in y[::-1]] for y in array]

#Splits an array in 2 along an axis and a position
def split_array(array, axis, pos):
    if axis == 'y':
        return [array[:pos], array[pos+1:]]
    elif axis == 'x':
        return [[[x for x in y[:pos]] for y in array], [[x for x in y[pos+1:]] for y in array]]

#Takes a 2D array and folds it on itself according to input instruction
def fold_array(array, instruction):
    axis = instruction[0]
    pos = instruction[1]

    array_split = split_array(array, axis, pos)
    array_top = array_split[0]
    array_bot = flip_array(array_split[1], axis)

    w_new, h_new = len(array_bot[0])-1, len(array_bot)-1
    array_folded = build_array(None, w_new, h_new)

    for y in range(h_new+1):
        for x in range(w_new+1):
            if array_top[y][x] == '#' or array_bot[y][x] == '#':
                array_folded[y][x] = '#'

    return array_folded

#Returns the amount of marked dots on a 2D array
def Q1_count_dots(array):
    return sum(sum(1 for x in y if x=='#') for y in array)


def main():
    with open("13\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        data_split = data_raw.split('\n\n')

        instructions = [x.split('=') for x in data_split[1].split('\n')]
        instructions = [(x[0][-1], int(x[1])) for x in instructions]

        puzzle_coords = [tuple(int(x) for x in y.split(',')) for y in data_split[0].split('\n')]

    #print(data_split)
    #print(instructions)
    #print(puzzle_coords)

    size = get_array_size(puzzle_coords)
    w = size[0]
    h = size[1]

    Q1_point_array = build_array(puzzle_coords, w, h)
    Q2_point_array = build_array(puzzle_coords, w, h)

    Q1_point_array = fold_array(Q1_point_array, instructions[0])

    for i in instructions:
        Q2_point_array = fold_array(Q2_point_array, i)

    #pprint.pprint(point_array)

    Q1_answer = Q1_count_dots(Q1_point_array)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer:")
    pprint.pprint(Q2_point_array, width=240)

if __name__ == "__main__":
    main()
    print(f"Execution time: {time.time()-START_TIME}")