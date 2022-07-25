#AOC9: find lowest points (basins) on the cavern floor
#Q1: Calculate risk factor by summing the basin depths + 1
#Q2: Multiply the size of 3 largest basins (areas bordered by height 9)

import time

START_TIME = time.time()


#Make a set of coordinates to use as starting points
#Any point in puzzle input with value 9
def find_starts(data):
    starting_coords = set()
    for y, row in enumerate(data):
        for x, n in enumerate(row):
            if n == 9:
                starting_coords.add((x, y))

    return starting_coords

#Start from every point at height 9, and crawl along towards any value lower than 9 in adjacent coordinates
#Basin found if every adjacent point is higher than the current point
#Plateaus are completely ignored and don't need separate handling
def find_basins(data):
    visited = set()
    basins = set()
    coords = find_starts(data)

    while True:
        new_coords = set()
        for c in coords:
            neighbor_values = []
            visited.add(c) #Keep track of already crawled nodes to avoid extra work
            '''
            Coordinate offsets
                  c[1]+1
            c[0]-1  c   c[0]+1
                  c[1]-1
            '''
            neighbors = (   (c[0]+1, c[1]),
                            (c[0]-1, c[1]),
                            (c[0], c[1]+1),
                            (c[0], c[1]-1))

            #Try-except handles literal edge-cases when a neighbor index is outside list range
            for n in neighbors:
                try:
                    if all(v >= 0 for v in n): #Negative indices work in python so make sure coords are positive
                        if (data[c[1]][c[0]] > data[n[1]][n[0]]) and (n not in visited):
                            new_coords.add(n)
                        neighbor_values.append(data[n[1]][n[0]])
                except IndexError:
                    continue
            
            #Check values of every neighbor coordinate if all() are higher, basin found
            if all(v > data[c[1]][c[0]] for v in neighbor_values):
                basins.add(c)
            
        coords = new_coords
        if len(coords) == 0:
            return basins

#Similar in function as find_basins(). Use a known basin as starting point, and begin growing/crawling the area until and edge (height value == 9) is found
#No checks needed this time, just add current node to the visited set() and keep going until no more nodes are discovered. 
def grow_basins(data, basins):
    visited = set()
    basin_areas = {}

    for i, b in enumerate(basins):
        visited = set()
        coords = {b} #set() but with initial value
        while True:
            new_coords = set()
            for c in coords:
                visited.add(c)
                neighbors = (   (c[0]+1, c[1]),
                                (c[0]-1, c[1]),
                                (c[0], c[1]+1),
                                (c[0], c[1]-1))

                for n in neighbors:
                    try:
                        if all(v >= 0 for v in n): #Negative indices work in python so make sure coords are positive
                            if (data[n[1]][n[0]] != 9) and (n not in visited):
                                new_coords.add(n)
                    except IndexError:
                        continue

            coords = new_coords
            if len(coords) == 0:
                break
        basin_areas[i] = visited

    return basin_areas
            

def Q1_calculate_risk(data, basins):
    risk = 0
    for b in basins:
        risk += data[b[1]][b[0]] + 1
    return risk
                    

def Q2_calculate_basin_areas(data, basins):
    basin_areas = grow_basins(data, basins)
    sizes = [len(x) for x in basin_areas.values()]
    Q2_answer = 1
    for i in range(3):
        largest_index = sizes.index(max(sizes)) #Get the index of largest value in list
        Q2_answer *= sizes.pop(largest_index) #Return largest value and remove from list
    return Q2_answer


def main():
    with open("9\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [[int(x) for x in y] for y in data_raw.split("\n")]

    basins = find_basins(puzzle_data)
    Q1_answer = Q1_calculate_risk(puzzle_data, basins)
    Q2_answer = Q2_calculate_basin_areas(puzzle_data, basins)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    print(f"Execution time: {time.time()-START_TIME}")
    #0.052858591079711914