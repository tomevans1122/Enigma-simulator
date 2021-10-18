import collections

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

# Created a pseudo-random ordering for rotors using random.shuffle(number_lst) and assigning numeral
I = [8, 21, 17, 11, 3, 15, 20, 22, 18, 14, 12, 10, 4, 23, 5, 1, 13, 25, 0, 6, 19, 24, 2, 9, 7, 16]
II = [21, 16, 3, 24, 10, 6, 23, 5, 15, 20, 22, 18, 7, 0, 12, 8, 1, 9, 4, 13, 2, 17, 25, 19, 11, 14]
III = [5, 15, 21, 24, 14, 25, 16, 11, 12, 22, 7, 20, 18, 8, 2, 23, 1, 17, 10, 4, 9, 3, 6, 0, 13, 19]
IV = [8, 20, 21, 10, 9, 5, 0, 11, 2, 12, 3, 25, 18, 6, 4, 16, 19, 22, 15, 1, 7, 23, 13, 24, 14, 17]
V = [23, 22, 12, 10, 1, 11, 17, 6, 0, 21, 19, 13, 8, 3, 4, 5, 9, 7, 2, 25, 16, 15, 14, 24, 20, 18]


# In reality, these are user inputted and changed daily. For simulation arbitrary choice will suffice.
test_plugboard_vals = [1, 2, 3, 11, 17, 15, 7, 8, 18, 14, 12, 10, 4, 23, 5, 22, 13, 25, 16, 6, 19, 24, 21, 9, 20, 0]
test_word = 'TURING'
rotor_choice = [I, II, III]     # choice of 5 rotors in any order
rotor_positions = [5, 2, 12]    # initial rotor settings for each rotor (i.e. letter pairings)


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

i = 0
encrypted_lst = []
while i < len(numbered_input):
    for num in numbered_input:
        plug1 = test_plugboard_vals[num]
        shuffled_rotor = shuffle_to_right(aligned_rotor1, i)
        rotor1 = shuffled_rotor[plug1]
        rotor2 = aligned_rotor2[rotor1]
        rotor3 = aligned_rotor3[rotor2]
        # now goes through the machine in reverse order
        reflected_rotor3 = aligned_rotor3[rotor3]
        reflected_rotor2 = aligned_rotor2[reflected_rotor3]
        reflected_rotor1 = shuffled_rotor[reflected_rotor2]
        reflected_plug = test_plugboard_vals[reflected_rotor1]
        encrypted_lst.append(reflected_plug)
        i += 1
        continue

# # Change numbers back into letters
encrypted_letters = []
for number in encrypted_lst:
    encrypted_letters.append(NTL_alphabet[number])

encryption = "".join(str(x) for x in encrypted_letters)

print(f"Your initial word: {test_word}\n"
      f"Your encrypted word: {encryption}")

