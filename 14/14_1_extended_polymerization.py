#AOC14: insert new elements between pairs of elements spoilers: exponential growth included
#Q1: Chain the polymers 10 times, count the individual elements and subtract fewest from most
#Q2: Same as Q1 but with 40 steps

import time

START_TIME = time.time()

#Initial approach. Just simulate adding elements between polymer pairs, even though I know what's coming
def Q1_count_commons(polymer_start, instructions, steps):
    counts = {x: polymer_start.count(x) for x in instructions.values()} #initialize the counting dictionary
    polymer_chain = polymer_start

    #Takes an input polymer string and inserts new elements between pairs according to given instructions
    def chain_polymer(polymer, _instructions):
        pairs = [f"{x[0]}{x[1]}" for x in zip(polymer, polymer[1:])] #Break the input string into pairs
        new_polymer = ''

        for pair in pairs:
            new_polymer += f'{pair[0]}{_instructions[pair]}'
            counts[_instructions[pair]] += 1
        new_polymer += polymer[-1]

        return new_polymer

    for i in range(steps):
        polymer_chain = chain_polymer(polymer_chain, instructions)

    return max(counts.values()) - min(counts.values())


#Figured out that the amount of pairs will be the same, no matter what their order is. As long as you know how many of each pair exists, 
#you can figure out how much of each element gets added in, and what new pairs it creates and removes
#That way, you don't need to keep track of a string that is gorillions of characters long
def Q2_count_commons(polymer_start, instructions, steps):
    individual_counts = {x: polymer_start.count(x) for x in instructions.values()} #Initialize element counts
    pair_counts = {x: 0 for x in list(instructions.keys())} #initialize pair counts with zeroes
    initial_pairs = [f"{x[0]}{x[1]}" for x in zip(polymer_start, polymer_start[1:])] #Break input string into pairs like in Q1

    #Initialize pair counts
    for p in initial_pairs:
        pair_counts[p] += 1

    for i in range(steps):
        pair_counts_new = dict(pair_counts)
        #For every pair that currently exists, get the added element from the instructions and add the amount of pairs to that element count
        #Subtract the same amount from current pairs
        for pair, amount in pair_counts.items():
            if amount != 0:
                addition = instructions[pair]
                individual_counts[addition] += amount
                pair_counts_new[pair] -= amount

                #Create 2 new pairs from current pair and the addition element, and add the current pair's amount to their amounts
                new_pair_1 = f"{pair[0]}{addition}" #f-strings are fun
                new_pair_2 = f"{addition}{pair[1]}"
                pair_counts_new[new_pair_1] += amount
                pair_counts_new[new_pair_2] += amount
                
        pair_counts = pair_counts_new
        
    return max(individual_counts.values()) - min(individual_counts.values())

def main():
    
    with open("14\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        data_split = data_raw.split('\n\n')

        polymer_start = data_split[0]
        instructions = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in data_split[1].split('\n')}

    Q1_answer = Q1_count_commons(polymer_start, instructions, 10)
    Q2_answer = Q2_count_commons(polymer_start, instructions, 40)
    
    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == '__main__':
    main()
    print(f"Execution time: {time.time() - START_TIME}")
    #Q2 time 0.0029916763305664062