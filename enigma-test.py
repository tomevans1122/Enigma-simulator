import unittest
import Enigma

class EnigmaProcess(unittest.TestCase):

    def test_rotors_length(self):
        # Make sure rotors all have 26 values
        rotor_choices = [Enigma.I, Enigma.II, Enigma.III, Enigma.IV, Enigma.V]
        for rotor in rotor_choices:
            self.assertEqual(len(rotor), 26)

    def test_rotors_do_not_repeat_integers(self):
        # Make sure rotor integers do not repeat
        rotor_choices = [Enigma.I, Enigma.II, Enigma.III, Enigma.IV, Enigma.V]
        for rotor in rotor_choices:
            self.assertTrue(rotor, set(rotor))

    def test_rotors_values_are_within_0_and_25(self):
        # Make sure rotor integers do not repeat
        rotor_choices = [Enigma.I, Enigma.II, Enigma.III, Enigma.IV, Enigma.V]
        i = 0
        while i < 26:
            for rotor in rotor_choices:
                self.assertIn(rotor[i], Enigma.number_lst)
            i += 1
            continue


    def test_plugboard_length(self):
        # Make sure plugboard has 26 values
        self.assertEqual(len(Enigma.test_plugboard_vals), 26)

    def test_input_is_string(self):
        # assert Enigma input is a string
        self.assertTrue(Enigma.test_word, type(''))

    def test_rotor_choice_is_correct(self):
        # assert the rotor choice consists of correct lists (i.e. the choice of rotors I,II,III,IV,V)
        # adjust this test as necessary if taking user input for rotor choice
        self.assertTrue(Enigma.I, Enigma.rotor_choice[0])

    def test_encryption_text_is_same_length_as_input_text(self):
        self.assertEqual(len(Enigma.numbered_input), len(Enigma.encrypted_lst))

    def test_input_letter_different_to_encrypted_letter(self):
        # the original enigma machines couldn't encrypt to the same letter, ensure this doesn't happen
        i = 0
        while i < len(Enigma.word_lst):
            self.assertNotEqual(Enigma.word_lst[i], Enigma.encrypted_letters[i])
            i += 1
            continue

if __name__ == '__main__':
    unittest.main()
