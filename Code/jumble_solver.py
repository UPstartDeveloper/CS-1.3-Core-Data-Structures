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


def determine_anagram(word, possible_anagram):
    """Determines if a word might be the anagram of another word.
       Credit for function comes from my CS 1.2 repo, can be found at
       https://github.com/UPstartDeveloper/CS-1.2-Intro-Data-Structures/blob/master/Code/anagram_app/app.py#L17

       Parameters:
       word(str)
       possible_anagram(str)

       Returns: bool

    """
    # possible_anagram cannot be a anagram if it isn't the same length as word
    if not len(word) == len(possible_anagram):
        return False
    # possible_anagram must be different from word
    elif word == possible_anagram:
        return False
    # possible_anagram must have all same letters as word
    for letter in possible_anagram:
        if letter not in word:
            return False

    for letter in word:
        if letter not in possible_anagram:
            return False
    # all tests passed, then return True
    return True


def possible_words(jumbled_word):
    """Returns the set of all anagrams of the jumbled word.

       Parameters:
       jumbled_word(str): the str that represents a common English word, with
                          its letters misspelled. This str has the following
                          key characteristics:
                          - it is composed entirely of English letters only
                          - letters may be repeated.
                          - all letters are lower case
                          - all letters will appear in correctly spelled word,
                            with the same distribution as in the input st

       Returns: Set: the set of all words that are anagrams of jumbled_word
    """
    # instaniate the set of all words with same length as jumbled_word
    set_same_length = get_words(len(jumbled_word))
    pass


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
