import collections
import math

# Letters to numbers and numbers to letters dictionaries
LTN_alphabet = {
    'A': '0',
    'B': '1',
    'C': '2',
    'D': '3',
    'E': '4',
    'F': '5',
    'G': '6',
    'H': '7',
    'I': '8',
    'J': '9',
    'K': '10',
    'L': '11',
    'M': '12',
    'N': '13',
    'O': '14',
    'P': '15',
    'Q': '16',
    'R': '17',
    'S': '18',
    'T': '19',
    'U': '20',
    'V': '21',
    'W': '22',
    'X': '23',
    'Y': '24',
    'Z': '25'
}
NTL_alphabet = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}
number_lst = [0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25]

# Original rotor values for German army enigma machines
I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
IV = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
V = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]

#reflector ordering before the signal passes back through rotors and plugboard again
Reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]

# turnover positions of each rotor in order
turnover_positions = [17, 5, 22]


# In reality, these are user inputted and changed daily. For simulation arbitrary choice will suffice.
test_plugboard_vals = [0, 24, 2, 3, 4, 5, 22, 7, 8, 9, 10, 12, 11, 16, 14, 15, 13, 17, 18, 19, 20, 21, 6, 23, 1, 25]
test_word = 'TURING'
rotor_choice = [I, II, III]     # choice of 5 rotors in any order
rotor_positions = [7, 24, 0]    # initial rotor settings for each rotor (i.e. letter pairings)


# Convert inputted string into a list
word_lst = []
i = 0
while i < len(test_word):
    word_lst.append(test_word[i])
    i += 1
    continue

# Change letters into corresponding alphabet numbers
numbered_input = []
for letter in word_lst:
    numbered_input.append(int(LTN_alphabet[letter]))

# Function to shift rotor positions by desired amount
def shuffle_to_right(x, y):
    lst = collections.deque(x)
    lst.rotate(y+1)
    shuffled_lst = list(lst)
    return shuffled_lst

# Aligning rotors to correct input settings by user
aligned_rotor1 = shuffle_to_right(rotor_choice[0], rotor_positions[0])
aligned_rotor2 = shuffle_to_right(rotor_choice[1], rotor_positions[1])
aligned_rotor3 = shuffle_to_right(rotor_choice[2], rotor_positions[2])

#ENIGMA PROCESS
# passing word through plugboard
def plugboard_or_reflector(plugboard_vals, numbered_word):
    plug_vals = []
    for i in numbered_word:
        plug_vals.append(plugboard_vals[i])
    return plug_vals

# shifting rotor each turn
def shift_rotor(aligned_rotor, n, rotor_num):
    if rotor_num == 1:
        n = -n % len(aligned_rotor)

    elif rotor_num == 2:
        n = - math.trunc(n / 25) % len(aligned_rotor)

    elif rotor_num == 3:
        n = - math.trunc(n / 675) % len(aligned_rotor)

    return shuffle_to_right(aligned_rotor, n)

# passing letters through the rotor (using shifting function)
def through_rotor(aligned_rotor, previous_sequence, rotor_num):
    number = []
    for i in range(len(previous_sequence)):
        rotation = shift_rotor(aligned_rotor, i, rotor_num)
        number.append(rotation[previous_sequence[i]])
    return number


def rotor_reverse(seq):
    rotor_rev = [0] * 26
    for i in range(26):
        rotor_rev[seq[i]] = i
    return rotor_rev


def through_rotor_reversed(aligned_rotor, previous_sequence, rotor_num):
    reversed_vals = []
    for i in range(len(previous_sequence)):
        rotation = shift_rotor(aligned_rotor, i, rotor_num)
        sequence_reverse = rotor_reverse(rotation)
        reversed_vals.append(sequence_reverse[previous_sequence[i]])
    return reversed_vals


# EXECUTION
SEQ1 = plugboard_or_reflector(test_plugboard_vals, numbered_input)
SEQ2 = through_rotor(aligned_rotor1, SEQ1, 1)
SEQ3 = through_rotor(aligned_rotor2, SEQ2, 2)
SEQ4 = through_rotor(aligned_rotor3, SEQ3, 3)
SEQ5 = plugboard_or_reflector(Reflector, SEQ4)
SEQ6 = through_rotor_reversed(aligned_rotor3, SEQ5, 3)
SEQ7 = through_rotor_reversed(aligned_rotor2, SEQ6, 2)
SEQ8 = through_rotor_reversed(aligned_rotor1, SEQ7, 1)
SEQ9 = plugboard_or_reflector(test_plugboard_vals, SEQ8)



# # Change numbers back into letters
encrypted_letters = []
for number in encrypted_lst:
    encrypted_letters.append(NTL_alphabet[number])

encryption = "".join(str(x) for x in encrypted_letters)

print(f"Your initial word: {test_word}\n"
      f"Your encrypted word: {encryption}")

