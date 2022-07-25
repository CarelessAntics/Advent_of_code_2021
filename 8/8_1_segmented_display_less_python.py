#Decode a scrambled 7-segment display
#Q1 Count the occurrences of unique digits in the output (the only numbers using a certain amount of segments on the display)
#Q2 Deduce the rest of the scrambled numbers and sum the decoded outputs

import time

START_TIME = time.time()


def alphabetize_a_to_z(string):
    return_string = ''
    letters_in_order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def Q1_count_unique(data):
    unique = [2, 4, 3, 7]
    count = 0
    for d in data:
        for out in d[1]:
            if len(out) in unique:
                count += 1
    return count

#Returns an integer of how many of the input characters match the input string
def chars_in_string(chars, string):
    count = 0
    for c in chars:
        if c in string:
            count += 1
    return count

'''
# of segments:
2: 1
3: 7
4: 4
5: 2, 3, 5
6: 0, 9, 6
7: 8
'''
#Deduce the key to unscramble the digits
def generate_key(display_unit):
    decode_key = {}
    unique_list = { 2: 1, 
                    3: 7,
                    4: 4,
                    7: 8}

    #Start with the easy ones. Add to dictionary the strings with unique lengths (i.e. not 5 or 6).
    for digit in display_unit[0]:
        digit_sorted = ''.join(sorted(digit)) #Alphabetize the digit string
        if len(digit) not in (5, 6):
            decode_key[unique_list[len(digit)]] = digit_sorted #use the unique_list to convert lengths into corresponding digits

    #Rest of the digits can be deduced by comparing them to previous known digits
    for digit in display_unit[0]:
        char_match_to_1 = chars_in_string(decode_key[1], digit)
        char_match_to_4 = chars_in_string(decode_key[4], digit)
        char_match_to_7 = chars_in_string(decode_key[7], digit)
        digit_sorted = ''.join(sorted(digit))
        
        if len(digit) == 6:
            if (char_match_to_4 == 4) and (char_match_to_7 == 3):
                decode_key[9] = digit_sorted
            elif (char_match_to_4 == 3) and (char_match_to_7 == 3):
                decode_key[0] = digit_sorted
            elif (char_match_to_4 == 3) and (char_match_to_7 == 2):
                decode_key[6] = digit_sorted

        if len(digit) == 5:
            if (char_match_to_1 == 1) and (char_match_to_4 == 2) and (char_match_to_7 == 2):
                decode_key[2] = digit_sorted
            elif (char_match_to_1 == 2) and (char_match_to_4 == 3) and (char_match_to_7 == 3):
                decode_key[3] = digit_sorted
            elif (char_match_to_1 == 1) and (char_match_to_4 == 3) and (char_match_to_7 == 2):
                decode_key[5] = digit_sorted

    decode_key_flipped = {v: k for k, v in decode_key.items()} #flip the dictionary for convenience
    return decode_key_flipped
            
#Generate a decoding key and unscramble the outputs 
def Q2_decode_output(data):
    output_sum = 0
    for d in data:
        decode_key = generate_key(d)
        new_number = 0
        for i, digit in enumerate(d[1]):      
            new_number += decode_key[''.join(sorted(digit))] * 10**(len(d[1])-i-1) #Changed from chaining strings to ints for SPEEEED

        output_sum += int(new_number)

    return output_sum

def main():
    with open("8\\puzzle_input.txt", "r") as f:
        data_raw = f.read()
        puzzle_data = [[x.split(' ') for x in y.split(' | ')] for y in data_raw.split('\n')]

    Q1_answer = Q1_count_unique(puzzle_data)
    Q2_answer = Q2_decode_output(puzzle_data)

    print(f"Q1 answer: {Q1_answer}")
    print(f"Q2 answer: {Q2_answer}")

if __name__ == "__main__":
    main()
    print(f"Execution took: {time.time()-START_TIME}")