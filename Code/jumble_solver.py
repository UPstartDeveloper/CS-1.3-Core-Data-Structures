def get_words():
    """Get words from the words file to get anagrams from."""
    # get words from the words file
    file = open("/usr/share/dict/words", "r")
    words_list = file.readlines()
    file.close()
    # removing newline characters from strings in words file
    words_no_newline = list()
    for word in words_list:
        word = word[:-3]
        words_no_newline.append(word)
    return words_no_newline


def unscramble(word):
    """Returns a common English word, given a string that consists solely of
       English letters.

       Parameters:
       word(str): a str composed entirely of English letters. No other types of
                  characters can appear. Letters may be repeated.
                  All lower case. All letters will appear in output str, and
                  in the same distribution as in the input str.

        Returns:
        str: the unscrambeld str

    """
    # store the number of characters in the input str
    num_letters = len(word)
    pass


if __name__ == "__main__":
