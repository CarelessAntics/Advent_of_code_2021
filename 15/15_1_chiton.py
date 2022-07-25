
import time

START_TIME = time.time()

def a_star(landscape):
    start = (0,0)
    end = (len(landscape[0])-1, len(landscape)-1)
    open_set = {start}
    previous = {}

    while True:
        current = paths[-1]
        for path in current:
            x, y = path[0], path[1]
            neighbors =((x+1, y),
                        (x-1, y),
                        (x, y+1),
                        (x, y-1))

def main():
    with open("15\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [[int(x) for x in y] for y in data_raw.split('\n')]

    #Q1_answer = Q1_simulate_octopus_steps(puzzle_data, 100)
    #Q2_answer = Q2_find_octopus_simultaneous(puzzle_data)

    #print(f"Q1 answer: {Q1_answer}")
    #print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    print(f"Execution time: {time.time()-START_TIME}")