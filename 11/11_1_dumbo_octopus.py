#AOC11: simulate flashing octopus herd behavior
#Q1: How many times do the octopuses flash in total within a set amount of time
#Q2: At which step do the octopodes synchronize their flashes

import pprint
import itertools
import time

START_TIME = time.time()

def Q1_simulate_octopus_steps(data, steps):
    flashes = 0
    octopodes_current = data[:]
    #print(0)
    #pprint.pprint(octopodes_current)

    for i in range(steps):
        #print(i+1)
        flashed = set()
        octopodes_current = [[x+1 for x in y] for y in octopodes_current]

        while True:
            octopodes_edit = octopodes_current[:]
            flash_happened = False
            for y, row in enumerate(octopodes_current):
                for x, octopus in enumerate(row):
                    neighbors = (   (x-1, y-1),
                                    (x-1, y),
                                    (x-1, y+1),
                                    (x, y-1),
                                    (x, y+1),
                                    (x+1, y-1),
                                    (x+1, y),
                                    (x+1, y+1))

                    if (octopus > 9) and ((x, y) not in flashed):
                        flash_happened = True
                        flashes += 1
                        flashed.add((x, y))
                        for n in neighbors:
                            if all(x >= 0 for x in n):    
                                try:
                                    octopodes_edit[n[1]][n[0]] += 1
                                except IndexError:
                                    continue
                                
            octopodes_current = octopodes_edit
            if not flash_happened:
                break
            
        for f in flashed:
            octopodes_current[f[1]][f[0]] = 0

        #print(i)
        #pprint.pprint(octopodes_current)

    return flashes

def Q2_find_octopus_simultaneous(data):
    octopodes_current = data[:]
    i = 0
    #print(0)
    #pprint.pprint(octopodes_current)

    while True:
        if len(set(itertools.chain.from_iterable(octopodes_current))) == 1:
            #print(set(itertools.chain.from_iterable(octopodes_current)))
            #print(f"simultaneous flash at {i}")
            return i
        #print(i+1)
        flashed = set()
        octopodes_current = [[x+1 for x in y] for y in octopodes_current]

        while True:
            octopodes_edit = octopodes_current[:]
            flash_happened = False
            for y, row in enumerate(octopodes_current):
                for x, octopus in enumerate(row):
                    neighbors = (   (x-1, y-1),
                                    (x-1, y),
                                    (x-1, y+1),
                                    (x, y-1),
                                    (x, y+1),
                                    (x+1, y-1),
                                    (x+1, y),
                                    (x+1, y+1))

                    if (octopus > 9) and ((x, y) not in flashed):
                        flash_happened = True
                        flashed.add((x, y))
                        for n in neighbors:
                            if all(x >= 0 for x in n):    
                                try:
                                    octopodes_edit[n[1]][n[0]] += 1
                                except IndexError:
                                    continue
                                
            octopodes_current = octopodes_edit
            if not flash_happened:
                break
            
        for f in flashed:
            octopodes_current[f[1]][f[0]] = 0

        i += 1

        

def main():
    with open("11\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [[int(x) for x in y] for y in data_raw.split('\n')]

    Q1_answer = Q1_simulate_octopus_steps(puzzle_data, 100)
    Q2_answer = Q2_find_octopus_simultaneous(puzzle_data)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    print(f"Execution time: {time.time()-START_TIME}")