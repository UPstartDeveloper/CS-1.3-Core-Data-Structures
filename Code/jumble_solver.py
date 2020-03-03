from set import Set
from linkedlist import LinkedList


def get_words(length):
    """Return the set of all words the same length as our input str.

       Parameter:
       length(int): the number of characters in the jumbled string

       Return:
       Set: an unordered collection of all words the same length as
            our jumbled str

    """
    # get words from the words file
    file = open("/usr/share/dict/words", "r")
    words_list = file.readlines()
    file.close()
    # removing newline characters from strings in words file
    clean_words = list()
    for word in words_list:
        word = word[:-3]
        clean_words.append(word)
    # return the set of all words with the appropiate length
    return Set(
        [word for word in clean_words if len(word) == length]
    )


def unscramble(word):
    """Returns a common English word, given a string that consists solely of
       English letters.

       Parameters:
       word(str): a str composed entirely of English letters. No other types of
                  characters can appear. Letters may be repeated.
                  All lower case. All letters will appear in output str, and
                  in the same distribution as in the input str.

        Returns:
        str: the unscrambled str

    """
    # store the number of characters in the input str
    num_letters = len(word)
    pass


if __name__ == "__main__":
