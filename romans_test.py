import unittest
import romans

class RomanNumberTest(unittest.TestCase):
    
    def test_symbols_romans(self):
        self.assertEqual(romans.roman_number_to_integer('I'), 1)
        self.assertEqual(romans.roman_number_to_integer('V'), 5)
        self.assertEqual(romans.roman_number_to_integer('X'), 10)
        self.assertEqual(romans.roman_number_to_integer('L'), 50)
        self.assertEqual(romans.roman_number_to_integer('C'), 100)
        self.assertEqual(romans.roman_number_to_integer('D'), 500)
        self.assertEqual(romans.roman_number_to_integer('M'), 1000)
        self.assertEqual(romans.roman_number_to_integer('K'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer(''), 'Format error')

    def test_repetitions(self):
        self.assertEqual(romans.roman_number_to_integer('II'), 2)
        self.assertEqual(romans.roman_number_to_integer('MMM'), 3000)
        self.assertEqual(romans.roman_number_to_integer('KKK'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer('MK'), 'Format error')

    def test_only_three(self):
        self.assertEqual(romans.roman_number_to_integer('IIII'), 'Format error')

    def test_falling_digits(self):
        self.assertEqual(romans.roman_number_to_integer('XVIII'), 18)
        self.assertEqual(romans.roman_number_to_integer('IL'), 'Format error')

if __name__ == '__main__':
    unittest.main()