#AOC12: Find paths through the cave system
#Q1: Find every path that traverses through smaller (lowercase) caves only once
#Q2: Same as Q1, but 1 small cave can be traversed twice

import time

START_TIME = time.time()

def build_node_grid(data):

    nodes = {}
    for d in data:
        if d[0] not in nodes.keys():
            nodes[d[0]] = [d[1]]
        elif (d[0] in nodes.keys()) and (d[1] not in nodes[d[0]]):
            nodes[d[0]].append(d[1])

        if d[1] not in nodes.keys():
            nodes[d[1]] = [d[0]]
        elif (d[1] in nodes.keys()) and (d[0] not in nodes[d[1]]):
            nodes[d[1]].append(d[0])

    return nodes


def Q1_find_all_paths(nodes):
    paths = []

    def traverse(nodes_inner: dict, previous: str, path=None):
        if path is None:
            path = []
        
        #print(previous)
        path.append(previous) 
        if previous == 'end':
            paths.append(path)
            return

        #print(path)
        for next in nodes_inner[previous]:
            newpath = path[:]
            if (next.islower() and next not in path) or (next.isupper()):
                traverse(nodes_inner, next, newpath)

    traverse(nodes, 'start')
    return len(paths)


def Q2_find_all_paths(nodes):
    paths = []

    def traverse(nodes_inner: dict, previous: str, path=None):
        if path is None:
            path = []
        
        path.append(previous)
        if previous == 'end':
            paths.append(path)
            return

        extra = all(path.count(k) < 2 for k in nodes_inner.keys() if (k.islower() and k not in ('start', 'end')))

        for next in nodes_inner[previous]:
            newpath = path[:]
            if (next.islower() and path.count(next) < 2 and next != 'start' and extra) or (next.isupper()):
                traverse(nodes_inner, next, newpath)
            elif (next.islower() and next not in path):
                traverse(nodes_inner, next, newpath)

    traverse(nodes, 'start')
    return len(paths)


def main():
    with open("12\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_input = [x.split('-') for x in data_raw.split('\n')]

    node_grid = build_node_grid(puzzle_input)
    Q1_answer = Q1_find_all_paths(node_grid)
    Q2_answer = Q2_find_all_paths(node_grid)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    print(f"Execution time: {time.time() - START_TIME}")