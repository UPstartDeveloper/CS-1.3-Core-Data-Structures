# !python


def letter_t(text, index_t):
    '''Return the letter at index_t (int) in text(list).'''
    try:
        return text[index_t].lower()
    # when the pattern is an empty str
    except IndexError:
        return ''


def letter_p(pattern, index_p):
    '''Return the letter at index_p(int) in pattern(str).'''
    try:
        return pattern[index_p].lower()
    # when the pattern is an empty str
    except IndexError:
        return ''


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # clean the text
    text = [char for char in text]
    # if pattern is empty, return True as default
    if len(pattern) == 0:
        return True
    # keep track of the index position we grab letters from the pattern
    else:
        index_p = 0
        # traverse the text for matches
        index_t = 0
        while index_t < len(text):
            # grab letters from the text and the pattern
            letter_text = letter_t(text, index_t)
            letter_pattern = letter_p(pattern, index_p)
            # if matching, move along in the pattern
            if letter_pattern == letter_text:
                # if the last letter in the pattern has matched, we found it!
                if index_p == (len(pattern) - 1):
                    return True
                else:
                    index_p += 1
            elif letter_text == letter_p(pattern, 0):
                index_p = 1
            # keep searching for matches of first letter, if no match
            else:
                index_p = 0
            index_t += 1
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
        # return 0 if pattern empty str
        if len(pattern) == 0:
            return 0
        # otherwise start searching for index!
        index_p = 0
        # traverse the text for matches
        index_t = 0
        while index_t < len(text):
            # grab letters from the text and the pattern
            letter_text = letter_t(text, index_t)
            letter_pattern = letter_p(pattern, index_p)
            # if matching, move along in the pattern
            if letter_pattern == letter_text:
                # if the last letter in the pattern has matched, we found it!
                if index_p == (len(pattern) - 1):
                    return index_t - index_p
                else:
                    index_p += 1
            elif letter_text == pattern[0]:
                index_p = 1
            # keep searching for matches of first letter, if no match
            else:
                index_p = 0
            index_t += 1
        # if no matches at the end, the pattern cannot be found
        return False


def find_next_index(text, pattern, indices):
    """Returns all indices in which a given patterns appears in a larger text.
       Implements recursion. Comparsions are case insensitive.

       Parameters:
       text(str): a string of alphanumeric chars. Mix of lower and uppercase.
                 May or may not include spaces. All ASCII chars are fair game.
       pattern(str): a shorter str which may or may appear in text.
                     Can simply be an empty string ('').
       indices(list): an ordered collection of the index positions in text,
                      where the pattern matches a substring of text.
                      If pattern = '', indices is all index positions in text.

       Returns: indices

    """
    index = find_index(text, pattern)
    if index is None:
        if len(indices) > 1:
            # update all indices to true values in the text str
            for i in range(1, len(indices)):
                # the index where an occurence begins, excluding the 1st
                next_index = indices[i]
                # adjusting this index to where it lies in the text str
                next_index += 1 + indices[i - 1]
                indices[i] = next_index
        return indices
    else:
        indices.append(index)
        # update the text to remove occurence of path that was just found
        text = text[index + 1:]
        return find_next_index(text, pattern, indices)


def find_all_indexes(text, pattern, indices=None):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # edge case: return every index if the pattern is an empty str
    if len(pattern) == 0:
        return [i for i in range(len(text))]
    # otherwise find all indices
    else:
        # set indices to an empty list on the first pass
        if indices is None:
            indices = list()
        # now find all the indices
        return find_next_index(text, pattern, indices)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
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
