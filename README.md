# Enigma-simulator

This repo is my attempt to create my own enigma enrcyption machine. It is designed to work in the same way as the Enigma machines used by the Germans in WW2. It simply takes in a word and encrypts it. The fact there is 158,962,555,217,826,360,000 possible settings is testament to the high level of encryption it provides.

## Set up

Firstly I convert the letters in the text into corresponding values in the alphabet (a = 0, b = 1, c = 2 etc). I then conduct the encryption before converting back into letters. In alignmant with the historical use of enigma machines, I have included a choice of five rotors (I-V) of which three are used at any one time and in an order desired by the user. These rotors are then set to a rotor setting, again chosen by the user, which decides the word pairings for each rotor. Finally there is a plugboard, where the user again chooses 10 letter pairings. Enigma is then ready to encrypt.

## Encryption

The first letter of the phrase is converted to an integer value, then passed through the plugboard. The value after being passed through the plugboard then passes through the first rotor, that outcome value is passed through the second rotor, that outcome is passed through the third rotor. The process then happens in reverse (as happened in the original enigma machines). That is the outcome from the third rotor goes back through the third rotor, that outcome goes through rotor 2, that outcome through rotor 1, that outcome through the plugboard. The last step is to convert the value from the plugboard back into its corresponding alphabet letter and we have our encrypted letter. 

This process is repeated for all the letters for an encrypted word.

