#Map out volcanic vents and find/count overlaps
#Q1: Solve for only horizontal and vertical lines
#Q2: Solve for all lines (diagonals are always 45deg)


def vec_sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

#Generate positions between 2 points. Only looks at vertical or horizontal lines
def generate_between_Q1(pair):
    start = pair[0]
    end = pair[1]
    vent_line = []
    if start[0] == end[0]:
        axis = 1
    elif start[1] == end[1]:
        axis = 0
    else:
        return None

    difference = vec_sub(end, start)[axis]
    d = int(difference / abs(difference)) #get sign
    for i in range(0, difference, d):
        entry = [None, None]
        entry[axis] = start[axis] + i
        entry[1-axis] = start[1-axis]
        vent_line.append(tuple(entry))

    vent_line.append(end)
    return vent_line

#Generate positions between 2 points. Looks at diagonals as well (always 45deg)
def generate_between_Q2(pair):
    start = pair[0]
    end = pair[1]
    vent_line = []

    difference = vec_sub(end, start)
    dx = int(difference[0] / abs(difference[0])) if difference[0] != 0 else 0 #get sign
    dy = int(difference[1] / abs(difference[1])) if difference[1] != 0 else 0 #get sign
    limit = max(abs(difference[0]), abs(difference[1]))
    for i in range(limit):
        x = start[0] + (i*dx)
        y = start[1] + (i*dy)
        vent_line.append((x, y))

    vent_line.append(end)
    return vent_line


def map_vents(data, q):
    ventmap = {}
    for d in data:
        if q == 'Q1':
            positions = generate_between_Q1(d)
        else:
            positions = generate_between_Q2(d)  
        #print(positions)
        if positions is None: 
            continue

        for p in positions:
            if p not in ventmap.keys():
                ventmap[p] = 1
            else:
                ventmap[p] += 1

    return ventmap
        


def main():

    with open("5\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_input = [[tuple(int(x) for x in y.split(',')) for y in z.split(' -> ')] for z in data_raw.split('\n')] #AAAAAAAAAAAAAAAAAAAAAAAA

    ventmap_Q1 = map_vents(puzzle_input, 'Q1')
    ventmap_Q2 = map_vents(puzzle_input, 'Q2')
    Q1_answer = len([x for x in ventmap_Q1.values() if x >= 2])
    Q2_answer = len([x for x in ventmap_Q2.values() if x >= 2])

    print(f"Q1 answer is {Q1_answer}")
    print(f"Q2 answer is {Q2_answer}")



if __name__ == "__main__":
    main()