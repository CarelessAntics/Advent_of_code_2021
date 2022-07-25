

def binary_to_decimal(bin):
    dec = 0
    for i, n in enumerate(bin[::-1]):
        dec += int(n) * 2**i

    return dec


def decimal_to_binary(dec):
    bin = ''
    div = dec
    while div >= 1:
        bin += str(div%2)
        div = int(div/2)

    return bin[::-1]

def bytes_most_common_Q1(data):

    common = ''
    uncommon = ''
    data_processed = zip(*data)
    for d in data_processed:
        d_int = tuple(int(i) for i in d)
        bit = round(sum(d_int)/len(d))
        common += str(bit)
        uncommon += str(int(not bit))

    return (common, uncommon)

#oxy == 1: oxygen, oxy == 0: co2
def find_ratings_Q2(data, oxy):

    data_elim = data[:]
    for i in range(len(data[0])):
        if len(data_elim) == 1:
            break

        data_new = []
        column = [int(x[i]) for x in data_elim]
        ones = column.count(1)
        zeroes = column.count(0)
        if oxy:
            c = int(ones > zeroes) if (ones != zeroes) else int(oxy)
        else:
            c = int(ones < zeroes) if (ones != zeroes) else int(oxy)
        
        for d in data_elim:
            if d[i] == str(c):
                data_new.append(d)

        data_elim = data_new[:]

    return data_elim[0]

def main():
    
    with open("3\\puzzle_input.txt", "r") as f:
        raw_data = f.read()
        puzzle_data = raw_data.split("\n")

    bytes_Q1 = bytes_most_common_Q1(puzzle_data)
    gamma_dec = binary_to_decimal(bytes_Q1[0])
    epsilon_dec = binary_to_decimal(bytes_Q1[1])

    oxygen = find_ratings_Q2(puzzle_data, 1)
    co2 = find_ratings_Q2(puzzle_data, 0)

    oxygen_dec = binary_to_decimal(oxygen)
    co2_dec = binary_to_decimal(co2)

    print(f"Q1 Answer: {gamma_dec * epsilon_dec}")
    print(f"Q2 Answer: {oxygen_dec * co2_dec}")


if __name__ == "__main__":
    main()