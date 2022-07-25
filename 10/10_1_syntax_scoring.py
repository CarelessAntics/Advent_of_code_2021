#AOC10: Fix corrupted syntax and incomplete lines of various parentheses
#Q1: Find and score corrupted lines (Find an incorrect closing parenthesis)
#Q2: Find and score incomplete lines, ignore corrupted (Find lines with parentheses left open)

import time

START_TIME = time.time()


#Make a dictionary of parentheses to easily match opening and closing pairs
#Go through each character and mark down every opening parenthesis (chunk start). When a closing parenthesis is encountered, match it with the last open chunk.
#If mismatch -> corrupted. Otherwise remove the last chunk and continue
def find_corrupted(data):
    errors = []
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    pairs = {x[0]:x[1] for x in list(zip(opening, closing)) + list(zip(closing, opening))}
    
    for line in data:
        chunks = []
        for char in line:
            if char in opening:
                chunks.append(char)
            if char in closing:
                if pairs[char] != chunks[-1]:
                    errors.append(char)
                    #print(f"Error on line {line} expected {pairs[chunks[-1]]}, but got {char} instead")
                    break
                else:
                    asd = chunks.pop(-1)

    return errors

#Similar to find_corrupted(), but instead skip over corrupted lines. 
#Once an uncorrupted line is finished, see if the chunk list has open chunks left unresolved
#If so, reverse the list and make a new one with corresponding pairs
def find_incomplete(data):
    missing = []
    corrupted = False
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    pairs = {x[0]:x[1] for x in list(zip(opening, closing)) + list(zip(closing, opening))}
    
    for line in data:
        chunks = []
        corrupted = False
        for char in line:
            if char in opening:
                chunks.append(char)
            if char in closing:
                if pairs[char] != chunks[-1]:
                    #print(f"Error on line {line} expected {pairs[chunks[-1]]}, but got {char} instead")
                    corrupted = True
                    break
                else:
                    asd = chunks.pop(-1)
        if (len(chunks) > 0) and not corrupted:
            missing.append([pairs[x] for x in reversed(chunks)])
        
    return missing


def Q1_corrupted_score(data):
    score = 0
    errors = find_corrupted(data)
    score_key = {   ')': 3, 
                    ']': 57, 
                    '}': 1197, 
                    '>': 25137}

    for char in [')', ']', '}', '>']:
        score += score_key[char] * errors.count(char)
    return score

def Q2_incomplete_score(data):
    scores = []
    missing = find_incomplete(data)
    score_key = {   ')': 1, 
                    ']': 2, 
                    '}': 3, 
                    '>': 4}
    
    for m in missing:
        score = 0
        for char in m:
            score = score * 5 + score_key[char]
        scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]



def main():
    with open("10\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = data_raw.split('\n')

    Q1_answer = Q1_corrupted_score(puzzle_data)
    Q2_answer = Q2_incomplete_score(puzzle_data)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    print(f"Execution completed in: {time.time()-START_TIME}")

    