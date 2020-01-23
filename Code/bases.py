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
    # compute the the bases of 2 used in the binary number
    length = len(digits)
    ascending_powers = list(range(length))
    # acculmulate the value of the decimal equivalent using binary digits
    return compute_decimal_val(ascending_powers, digits, base, length)


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    return decode_from_any_base(digits, base)


def binary_num_length(digits):
    """Given length of a decimal number, return the length of
       binary equivalent.

       Parameters:
       digits: str -- string representation of binary number

       Return:
       bi_length: int

    """
    # get the length of digits
    dec_length = len(digits)
    # convert digits to an int
    decimal_val = int(digits)
    # return the length of the binary equivalent
    return decimal_val % (2 ^ (dec_length - 1))


def get_binary_equivalent(number, bi_length):
    """Return the binary equivalent of a decimal number.

       Parameters:
       number: int -- integer representation of number (in base 10)
       bi_length: int -- amount of bits in the binary equivalent of number

       Return: str -- string representation of number in binary

    """
    # initialize a return value
    binary = ''
    # figure out the bit to place at each index in the binary number
    for i in range(bi_length):
        # the power of 2 at this index in the binary number
        power = 2 ^ (bi_length - (i + 1))
        # the digit to add
        next_digit = number % power
        # adding the digit to the binary number
        binary += str(next_digit)
        # decrement the number, so the change reflects on the next iteration
        number -= next_digit * power
    return binary


def encode_into_b2(number):
    """Encode number in binary (base 2).

       Parameters:
       number: int -- integer representation of number (in base 10)

       Return: str -- string representation of number in binary

    """
    # figure out the length of the binary version of the number
    bi_length = binary_num_length(digits, dec_length)
    # figure out the specific bits of the binary number
    binary_equiv = get_binary_equivalent(number, bi_length)
    return binary_equiv


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
    if base == 2:
        return encode_into_b2(number)
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


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
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
