romans = {'M': 1000,
         'D': 500,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1,
}

existing = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

def roman_number_to_integer(roman_number):
    if roman_number == '':
        return 'Format error'

    integer = 0
    repeated_number = 1
    previous_letter = ''
    was_subtraction = False

    for letter in roman_number:
        if letter in romans:
            if previous_letter == '' or romans[previous_letter] >= romans[letter]:
                integer += romans[letter]
                was_subtraction = False
            else:
            
                if previous_letter + letter in existing and repeated_number < 2 and not was_subtraction:
                    integer = integer - romans[previous_letter] * 2 + romans[letter]
                    was_subtraction = True
                else:
                    return 'Format error'       
        else:
            return 'Format error'

        if letter == previous_letter and repeated_number == 3:
            return 'Format error'
        elif letter == previous_letter :
            repeated_number += 1
        else:
            repeated_number = 1

        previous_letter = letter
    
    return integer