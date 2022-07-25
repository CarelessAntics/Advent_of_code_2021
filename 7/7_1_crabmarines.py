#Calculate fuel consumption of crab-piloted submarines
#Q1 Find lowest fuel consumption when consumption rate is assumed linear
#Q2 Find lowest fuel consumption when consumption rate increases through distance traveled


import sys
import time

START_TIME = time.time()

#Cycle through possible starting positions, count fuel consumption and return lowest value
def get_lowest_consumption_Q1(data):
    min_fuel = sys.maxsize * 2 + 1 #python version of Integer.MAX_VALUE
    for pos in range(max(data) + 1):
        fuel = 0
        for d in data:
            fuel += abs(d-pos)
            #Move to next position if consumption exceeds current minimum, no need to keep going otherwise
            if fuel > min_fuel: break 

        min_fuel = min(min_fuel, fuel)

    return min_fuel

#Same as the Q1 function, with 1 line changed. Slow as FUCK
def get_lowest_consumption_Q2(data):
    min_fuel = sys.maxsize * 2 + 1
    for pos in range(max(data) + 1):
        fuel = 0
        for d in data:
            fuel += sum(range(abs(d-pos) +1)) #Python magic. Create an iterable (0, 1, 2, 3, ... , distance) and get its sum
            if fuel > min_fuel: break

        min_fuel = min(min_fuel, fuel)
    return min_fuel
    

def main():
    with open("7\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [int(x) for x in data_raw.split(',')]

    #print(puzzle_data)
    Q1_answer = get_lowest_consumption_Q1(puzzle_data)
    Q2_answer = get_lowest_consumption_Q2(puzzle_data)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

    
if __name__ == "__main__":
    main()
    print(f"Execution took: {time.time() - START_TIME}")
    #Q2 exection time: 5.2490456104278564 ;__;