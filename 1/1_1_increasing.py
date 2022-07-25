#Q1 Check how many times depth measurements increase
#Q2 "Denoise" the data by summing the elements in steps of 3 and checking the sums for increases

def main():

    with open("1\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = data_raw.split("\n")
        puzzle_data = [int(d) for d in puzzle_data]

    #Make pairs with list comprehension by offsetting and zipping the same list
    #Do the comparisons directly in the comprehension and get the answer from list length
    data_list_Q1 = [d for d in zip(puzzle_data, puzzle_data[1:]) if d[0] < d[1]]
    data_list_Q2 = [d[0] + d[1] + d[2] for d in zip(puzzle_data, puzzle_data[1:], puzzle_data[2:])]

    count_Q1 = len(data_list_Q1)
    count_Q2 = len([d for d in zip(data_list_Q2, data_list_Q2[1:]) if d[0] < d[1]])

    print(f"Task one answer: {count_Q1}")
    print(f"Task two answer: {count_Q2}")
    
    
if __name__ == "__main__":
    main()