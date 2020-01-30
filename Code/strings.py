from palindromes import clean_text
# !python


def letter_t(text, index_t):
    '''Return the letter at index_t (int) in text(list).'''
    return text[index_t]


def letter_p(pattern, index_p):
    '''Return the letter at index_p(int) in pattern(str).'''
    return pattern[index_p]


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # clean the text
    text = clean_text(text)
    # if pattern is empty, return True as default
    if len(pattern) == 0:
        return True
    # keep track of the index position we grab letters from the pattern
    else:
        index_p = 0
        # traverse the text for matches
        for index_t in range(len(text)):
            # grab letters from the text and the pattern
            letter_text = letter_t(text, index_t)
            letter_pattern = letter_p(pattern, index_p)
            # if matching, move along in the pattern
            if letter_pattern == letter_text or letter_text == pattern[0]:
                # if the last letter in the pattern has matched, we found it!
                if (index_p + 1) == len(pattern):
                    return True
                else:
                    index_p += 1
            # keep searching for matches of first letter, if no match
            else:
                index_p = 0
        # if no matches at the end, the pattern cannot be found
        return False


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # find out if the pattern exist
    if contains(text, pattern) is False:
        return None
    else:
        # begin str traversal!
        index_t = 0
        while index_t < len(text):
            # try to find a match for the first letter of pattern
            pattern_length_without_first = len(pattern) - 1
            if letter_t(text, index_t) == letter_p(pattern, 0):
                # make sure the rest of the pattern also matches
                for i in range(1, len(pattern)):
                    if not letter_t(text, index_t + i) == letter_p(pattern, i):
                        # move ahead to the next possible place for matching
                        index_t += pattern_length_without_first
                    elif i == pattern_length_without_first:
                        return i
            # don't give up! move to the next possible index for matching
            else:
                index_t += 1
        return index_t


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
