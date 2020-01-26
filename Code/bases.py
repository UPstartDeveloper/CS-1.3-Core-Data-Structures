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

       Return: int -- the decimal representation of the value of digit
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
        return int(digit)


def compute_decimal_val(ascending_powers, digits, base, length):
    """Return the representation of a number in the base 10 system.

       Parameters:
       ascending_powers: list -- a collection of the exponents used in place
                                values of the digits number
       digits: str -- string representation of number (in given base)
       base: int -- base of given number
       length: int -- the length of the part of digits, left to be decoded

       Return: int -- integer representation of number (in base 10)
    """
    # init a return value
    decimal_value_of_whole_num = 0
    for power in ascending_powers:
        decimal_value_of_single_digit = convert_digit_to_decimal(digits[power])
        decimal_value_of_whole_num += (
            math.pow(base, (length - 1)) * decimal_value_of_single_digit)
        # move down the exponent for the next iteration
        length -= 1
    return decimal_value_of_whole_num


def decode_from_any_base(digits, base):
    """Decode digits from any base (2 up to 36).

       Parameters:
        digits: str -- string representation of number (in given base)
        base: int -- base of given number

        Return: int -- integer representation of number (in base 10)

    """
    # compute the powers of the old base used in the representation of digits
    length = len(digits)
    ascending_powers = list(range(length))
    # acculmulate the value of the decimal equivalent using digits in new base
    return compute_decimal_val(ascending_powers, digits, base, length)


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    return decode_from_any_base(digits, base)


"""
Encoding functions
"""


def get_num_length(number, base):
    """Given length of a decimal number, return the length of the
       equivalent representation in the new base.

       Parameters:
       number: int -- string representation of number
       base: int -- base to convert to

       Return:
       bi_length: int

    """
    exponent = 0
    power = -1
    # count the number of powers of the base needed to exceed the number
    while power <= number:
        exponent += 1
        power = math.pow(base, exponent)
    # the exponent shows the amount of place values in the number being encoded
    return (exponent)


def get_equivalent(number, base, new_num_length):
    """Return the equivalent of a decimal number in the new base.

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
    # figure out the bit to place at each index in the new number
    for i in range(new_num_length):
        # the power of the new base, at this index in the new number
        place_value = math.pow(base, (new_num_length - (i + 1)))
        # the decimal representation of the digit to add
        next_digit = int(number // place_value)
        # convert to representation of that value for the appropiate base
        if next_digit > 9:
            index_of_digit = next_digit - 10
            # adding the digit to the new  number
            new_value += alpha[index_of_digit]
        else:
            new_value += str(next_digit)
        # decrement the number, so the change reflects on the next iteration
        number -= next_digit * place_value
    return new_value


def encode_whole_number(number, base):
    """Encode number into any base 2-36. Must be a whole number.

       Parameters:
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       Return: str -- string representation of number

     """
    # figure out the length of the inputted version of the number
    new_num_length = get_num_length(number, base)
    # figure out the specific digits of the new representation of number
    equivalent_value = get_equivalent(number, base, new_num_length)
    return equivalent_value


def get_sig_figs(num, index_of_point):
    """Return the number of digits to include after the radix point.

      Parameters:
       num: str -- representation of number (in base 10)
       index_of_point: int -- index position of the radix point in num

      Return: int -- number of digits appearing after the point in number

    """
    digits_after_point = len(num[(index_of_point + 1):])
    return digits_after_point


def encode_fraction(num_digits, number, base):
    """Handles conversion of the non-integer portion of a fractional number.

       Parameters:
       num_digits: int -- the number of digits to include in the return value
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       Return: str -- representation of the number in the new base
    """
    # init return str
    new_repr = ''
    for i in range(num_digits):
        # multiply number by the new base
        scaled_num = number * base
        # find the index of the radix point
        str_scaled_num = str(scaled_num)
        index = str_scaled_num.index('.')
        # add the int portion to the return value
        integer_portion = str_scaled_num[:index]
        new_repr += integer_portion
        # use the decimal portion to multiply by the base, on next iteration
        decimal_portion = int(str_scaled_num[(index + 1):])
        number = decimal_portion
    return new_repr


def encode_fractional_number(number, base):
    """Encode number into any base 2-36. Must be a fractional number.

       Parameters:
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       Return: str -- string representation of number in the new base

     """
    # init return value
    new_num = ''
    # add the digits that come before the radix index_of_point
    num_as_str = str(number)
    index_of_point = num_as_str.index('.')
    # convert only the slice of the number that appears before the point
    num_before_point = math.floor(number)
    new_num += encode_whole_number(num_before_point, base)
    # add the radix point
    new_num += '.'
    # the answer will have same number of digts after radix point as input
    num_digits_after_point = get_sig_figs(num_as_str, index_of_point)
    # add the digits that come after the radix point, and return
    new_num += encode_fraction(num_digits_after_point, number, base)
    return new_num


def encode_into_any_base(number, base):
    """Encode number into any base 2-36. Can be fractional or whole.

       Parameters:
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       Return: str -- string representation of number in the new base

    """
    # enocding numbers if it's not fractional
    if number % 1 == 0:
        return encode_whole_number(number, base)
    # encoding numbers that are fractional
    else:
        return encode_fractional_number(number, base)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
       number: int -- integer representation of number (in base 10)
       base: int -- base to convert to

       return: str -- string representation of number (in given base)

    """
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    return encode_into_any_base(number, base)


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
    # decode into base 10 representation, if not already so
    if not base1 == 10:
        digits = decode(digits, base1)
    # from base 10, encode into the requested base
    return encode(int(digits), base2)


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
