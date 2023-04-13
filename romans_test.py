import unittest
import romans

class RomanNumberTest(unittest.TestCase):
    def test_create_roman_numeral(self):
        rn = romans.RomanNumber(25)
        self.assertEqual(rn.valor, 25)
        self.assertEqual(rn.rValor, 'XXV')

        snr = romans.RomanNumber('XIV')
        self.assertEqual(snr.valor, 14)
        self.assertEqual(snr.rValor, 'XIV')
        

        tnr = romans.RomanNumber('XXXX')
        self.assertEqual(tnr.valor, 'Format error')
        self.assertEqual(tnr.rValor, 'Format error')

        cnr = romans.RomanNumber(0)
        self.assertEqual(cnr.valor, 'Overflow')
        self.assertEqual(cnr.rValor, 'Overflow')

        qnr = romans.RomanNumber(4000)
        self.assertEqual(qnr.valor, 'Overflow')
        self.assertEqual(qnr.rValor, 'Overflow')

if __name__ == '__main__':
    unittest.main()