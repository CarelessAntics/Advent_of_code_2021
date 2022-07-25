


def navigate(nav_data):
    pos = 0
    depth = 0
    aim = 0
    for d in nav_data:
        value = int(d[1])
        if d[0] in ("down", "up"):
            if d[0] == "down":
                #depth += value #uncomment for Q1
                aim += value
            else:
                #depth -= value #uncomment for Q1
                aim -= value
        else:
            pos += value
            depth += aim * value #Comment out for Q1

    return (pos, depth)

def main():

    with open("2\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [tuple(d.split(' ')) for d in data_raw.split('\n')]

    nav_position = navigate(puzzle_data)    
    Q_answer = nav_position[0] * nav_position[1]
    print(f"Q answer: {Q_answer}")


if __name__ == "__main__":
    main()