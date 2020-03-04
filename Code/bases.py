#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


"""
Decoding functions
"""


def convert_digit_to_decimal(digit):
    """Compute the base-10 representation of a digit from a non-base 10 number.

       Parameters:
       digit: str -- can be any symbol used to represent a digit in a number,
                     base 2-36

       Return: float -- the decimal representation of the value of digit
    """
    # list of all English letters
    alpha = list(string.ascii_lowercase)
    # if digit a letter
    if digit in alpha:
        for i in range(len(alpha)):
            if digit.lower() == alpha[i]:
                # return the sum of 10, and the index of the letter in alphabet
                return 10 + i
    # if the number is 0-9, it's decimnal representation is no different
    else:
        return float(digit)


def compute_decimal_val_for_whole_num(digits, base):
    """Return the representation of a number in the base 10 system.

       Parameters:
       digits: str -- string representation of number (in given base)
       base: int -- base of given number

       Return: int -- integer representation of number (in base 10)
    """
    # init a return value
    decimal_value_of_overall_num = 0
    # compute the powers of the old base used in the representation of digits
    length = len(digits)
    # i represents the exponent the base is raised at for a given place value
    for i in range(length):
        # grab the next symbol - a digit, a sign, a radix point
        next_symbol = digits[i]
        if not next_symbol == '.':
            decimal_value_of_single_digit = float(
                convert_digit_to_decimal(next_symbol))
            decimal_value_of_overall_num += (
                math.pow(base, (length - 1)) * decimal_value_of_single_digit)
            # move down the exponent for the next iteration
            length -= 1
        else:
            pass
    return decimal_value_of_overall_num


def compute_decimal_val_for_fractional_num(digits, base):
    """Return the representation of a number in the base 10 system.

       Parameters:
       digits: str -- string representation of number (in given base)
       base: int -- base of given number

       Return: int -- integer representation of number (in base 10)
    """
    # init a return value
    decimal_value_of_overall_num = 0
    # compute the powers of the old base used in the representation of digits
    length = len(digits) - 2
    # keep track of the index we are at in the number, start fter radix point
    index = 2
    # i represents the exponent the base is raised at for a given place value
    for i in range(1, length + 1):
        # grab the next symbol - a digit, a sign, a radix point
        next_symbol = digits[index]
        if not next_symbol == '.':
            decimal_value_of_single_digit = (
                convert_digit_to_decimal(next_symbol))
            decimal_value_of_overall_num += (
                math.pow(base, -i) * decimal_value_of_single_digit)
            # move to next digit for next iteration
            index += 1
        else:
            index += 1
    return decimal_value_of_overall_num


def decode_from_any_base(digits, base, decoded_num):
    """Decode digits from any base (2 up to 36).

       Parameters:
        digits: str -- string representation of number (in given base)
        base: int -- base of given number
        decoded_num: float -- representation of number (in base 10)

        Return: decoded_num
    """
    # determine if the digits contain a fraction
    if '.' in digits:
        # spearate the int and fractional portions of the number
        index_of_point = digits.index('.')
        int_portion = digits[:index_of_point]
        fractional = digits[index_of_point:]
        # decode the int part
        if not int_portion == '0':
            decoded_num += compute_decimal_val_for_whole_num(int_portion, base)
            # update the part of the number that's been decoded so far
            digits = '0' + fractional
            # now call the function again!
            return decode_from_any_base(digits, base, decoded_num)
        elif not fractional == '.0':
            # decode the fractional number, can be leftover from a mixed number
            decoded_num += compute_decimal_val_for_fractional_num(digits, base)
            return decoded_num
    else:
        # just take care of the integer
        return int(compute_decimal_val_for_whole_num(digits, base))


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: float -- representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # init return value
    decoded_num = 0
    # decode the number
    return decode_from_any_base(digits, base, decoded_num)


"""
Encoding functions
"""


def get_num_length_for_whole(number, base):
    """Given length of a natural decimal number, return the length of the
       equivalent representation in the new base.

       Parameters:
       number: int -- string representation of number
       base: int -- base to convert to

       Return:
       exponent: int -- the highest exponent of a place value needed

    """
    exponent = 0
    power = -1
    # count the number of powers of the base needed to exceed the number
    while power <= number:
        exponent += 1
        power = math.pow(base, exponent)
    # the exponent shows the amount of place values in the number being encoded
    return (exponent)


def get_num_length_for_fractional(number, base):
    """Given length of a fractional decimal number, return the length of the
       equivalent representation in the new base.

       Parameters:
       number: float -- representation of number
       base: int -- base to convert to

       Return:
       exponent: int -- the highest exponent of a place value needed

    """
    exponent = 0
    power = 0
    sum = 0
    # count the number of powers of the base needed to exceed the number
    while sum <= number:
        exponent -= 1
        power = math.pow(base, exponent)
        sum += number
    # the exponent shows the amount of place values in the number being encoded
    return -(exponent - 1)


def get_equivalent_for_integers(number, base, new_num_length):
    """Return the equivalent of a decimal number in the new base. Only integers
       allowed.

       Parameters:
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to
       new_num_length: int -- how many digits needed in the encoded number

       Return: str -- string representation of number

    """
    # initialize a return value
    new_value = ''
    # list of all English letters
    alpha = list(string.ascii_lowercase)
    # figure out the digit to place at each index in the new number
    for i in range(new_num_length):
        # each iteration the power of the place value decreases
        place_value = math.pow(base, (new_num_length - (i + 1)))
        # the representation of the next digit to add in the new base
        next_digit = int(number // place_value)
        # convert to representation of that value for the appropiate base
        if next_digit > 9:
            index_of_digit = next_digit - 10
            # adding the digit to the new number
            new_value += alpha[index_of_digit]
        else:
            new_value += str(next_digit)
        # decrement the number, so the change reflects on the next iteration
        number -= next_digit * place_value
    return new_value


def get_equivalent_for_fractions(number, base, new_num_length):
    """Return the equivalent of a decimal number in the new base. Only floating
       point numbers allowed.

       Parameters:
       number: float -- integer representation of number (in base 10)
       base: int -- base to convert to
       new_num_length: int -- how many digits needed in the encoded number

       Return: str -- string representation of number

    """
    # initialize a return value
    new_value = ''
    # list of all English letters
    alpha = list(string.ascii_lowercase)
    # keep track of the exponent for the place value currently being converted
    exponent = -1
    # for decimals, powers descend from left to right
    for i in range(-new_num_length, 0):
        # for place values, absolute value of the power increases left to right
        place_value = math.pow(base, exponent)
        exponent -= 1
        # the representation of the next digit to add in the new base
        next_digit = int(number // place_value)
        # convert to representation of that value for the appropiate base
        if next_digit > 9:
            index_of_digit = next_digit - 10
            # adding the digit to the new number
            new_value += alpha[index_of_digit]
        else:
            new_value += str(next_digit)
        # decrement the number, so the change reflects on the next iteration
        number -= next_digit * place_value
        # print(number)
    return new_value


def encode_whole_number(number, base):
    """Encode number into any base 2-36. Must be a whole number.

       Parameters:
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       Return: str -- string representation of number

     """
    # figure out the length of the inputted version of the number
    new_num_length = get_num_length_for_whole(number, base)
    # figure out the specific digits of the new representation of number
    equivalent_value = get_equivalent_for_integers(number, base,
                                                   new_num_length)
    return equivalent_value


def encode_fractional_number(number, base):
    """Encode number into any base 2-36. Must be a fractional number.

       Parameters:
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       Return: str -- string representation of number in the new base

    """
    # figure out the length of the inputted version of the number
    new_num_length = get_num_length_for_fractional(number, base)
    # figure out the specific digits of the new representation of number
    equivalent_value = get_equivalent_for_fractions(number, base,
                                                    new_num_length)
    return equivalent_value


def encode_into_any_base(number, base, encoded_num):
    """Encode number into any base 2-36. Can be fractional or whole.

       Parameters:
       number: float -- integer representation of number (in base 10)
       base: int -- base to convert to
       encoded_num: str -- representation (so far) of number in base

       Return: str -- string representation of number in the new base

    """
    # enocding numbers if it's not fractional
    if number % 1 == 0:
        return encode_whole_number(number, base)
    # encoding numbers that are fractional
    else:
        # first encoding the part that comes before the radix point
        if not str(number)[0] == '0':
            int_part = math.floor(number)
            encoded_num += encode_whole_number(int_part, base)
            # now cut off the integer from number, so it's just a fraction
            number = number - int_part
            # then encoding the decimal part of the number
            return encode_into_any_base(number, base, encoded_num)
        else:
            # add the radix point to the answer
            if encoded_num == '':
                encoded_num += '0'
            encoded_num += '.'
            # convert the fractional part (of the overall number being encoded)
            encoded_num += encode_fractional_number(number, base)
            return encoded_num


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
       number: float -- integer representation of number (in base 10)
       base: int -- base to convert to

       return: str -- string representation of number (in given base)

    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # init return value
    encoded_num = ''
    # call recursive function to encode numbers
    return encode_into_any_base(number, base, encoded_num)


"""
Converting functions
"""


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # if we're converting to base 10, only need to do a decode operation
    if base2 == 10:
        # take off the first digit to decide sign later
        sign = digits[0]
        # convert rest of digits
        final_value = str(decode(digits[1:], base1))
        # now add sign to the final return value
        if sign == '0':
            return final_value
        elif sign == '1':
            return '-' + final_value
        else:
            return "Invalid binary number."
    else:
        # decode into base 10 representation, if not already so
        if not base1 == 10:
            digits = decode(digits, base1)
        # from base 10, encode into the requested base
        return encode(float(digits), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {} (with sig figs)'.format(digits,
                                                                      base1,
                                                                      result,
                                                                      base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
