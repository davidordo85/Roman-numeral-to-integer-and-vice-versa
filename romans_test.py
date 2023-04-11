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
        self.assertEqual(romans.roman_number_to_integer('XI'), 11)
        self.assertEqual(romans.roman_number_to_integer('XV'), 15)
        self.assertEqual(romans.roman_number_to_integer('XX'), 20)
        self.assertEqual(romans.roman_number_to_integer('CI'), 101)

    def test_digits_remain(self):
        self.assertEqual(romans.roman_number_to_integer('XC'), 90)
        self.assertEqual(romans.roman_number_to_integer('XD'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer('XM'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer('IL'), 'Format error')

    def test_dont_subtract_from_multiples_of_5(self):
        self.assertEqual(romans.roman_number_to_integer('VC'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer('XCV'), 95)

    def test_subtraction_a_single_symbol(self):
        self.assertEqual(romans.roman_number_to_integer('XXL'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer('IXL'), 'Format error')
        self.assertEqual(romans.roman_number_to_integer('XXX'), 30)

if __name__ == '__main__':
    unittest.main()