romans = {'M': 1000,
         'D': 500,
         'C': 100,
         'L': 50,
         'X': 10,
         'V': 5,
         'I': 1,
         '': None
}

def roman_number_to_integer(roman_number):
    if roman_number == '':
        return 'Format error'

    integer = 0
    repeated_number = 1
    previous_letter = ''
    for letter in roman_number:
        if letter == previous_letter and repeated_number == 3:
            return 'Format error'
        elif letter == previous_letter:
            repeated_number += 1
        else:
            repeated_number = 1

        if letter in romans:
            integer += romans[letter]
        else:
            return 'Format error'

        previous_letter = letter

    return integer
