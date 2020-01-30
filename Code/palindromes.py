#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def clean_text(text):
    '''Given a str, returns a list of alphanumeric chars in the str.'''
    return [char.lower() for char in text if char.isalpha() is True]


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # clean the string
    letters = clean_text(text)
    # calculate the midpoint of the str
    halfway_point = (len(letters) // 2)
    # case-insensitive checking from front and back
    for i in range(halfway_point):
        letter = letters[i].lower()
        letter_from_back = letters[-i-1]
        if not letter == letter_from_back:
            return False
    # if you made it through, it's a palindrome
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # on first stack frame, clean text str and set left to the first letter
    if left is None:
        left = 0
        text = clean_text(text)
    # identify the middle index position
    halfway_point = len(text) // 2
    if halfway_point > 0:
        # grab the letters we need to compare, case insensitive
        right = (-left - 1)
        letter_left = text[left].lower()
        letter_right = text[right].lower()
        # make the comparision, and decide to check more letters or not
        if letter_left == letter_right:
            if left < halfway_point:
                return is_palindrome_recursive(text=text, left=left+1)
            else:
                return True
        # one mismatch is all we need to know the str is not a palindrome
        else:
            return False
    # if there are no letters, True returned by default
    else:
        return True
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
