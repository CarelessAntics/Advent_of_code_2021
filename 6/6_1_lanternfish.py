#Approximate fish breeding rate
#Find out fish population after 80 days
#Find out fish population after 256 days
import time
#START_TIME = time.time()


#naive approach, simulate the status of every fish. Falls apart time-wise in Q2
def simulate_fish_Q1(data, days):
    fishes = data[:]
    for i in range(days):
        newborns = 0
        for j, fish in enumerate(fishes):
            if fish == 0:
                newborns += 1
                fishes[j] = 6
            else:
                fishes[j] -= 1

        fishes += [8] * newborns
        #print(fishes)
    return fishes

#Only keep track of how many fish are in what part of their breeding cycle using a dictionary
def calculate_fish_Q2(initial, days):
    #Initialize the fish counts
    fish_counts = {x: 0 for x in range(9)}
    for i in initial:
        fish_counts[i] += 1

    for day in range(days):
        helper_dict = {x: 0 for x in range(9)}
        newborns = 0

        for key in fish_counts.keys():
            if key == 0:
                newborns += fish_counts[key]
                #helper_dict[6] += fish_counts[key]
            else:
                helper_dict[key-1] = fish_counts[key]

        #Add newborns to both 6-day and 8-day fish counts
        helper_dict[8] += newborns
        helper_dict[6] += newborns
        fish_counts = helper_dict
        #print(fish_counts)

    return fish_counts
            

def main():
    with open("6\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [int(x) for x in data_raw.split(',')]

    Q1_answer = len(simulate_fish_Q1(puzzle_data, 80))
    Q2_answer = sum(calculate_fish_Q2(puzzle_data, 256).values())

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    #print(time.time() - START_TIME)