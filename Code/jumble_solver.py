from set import Set
from linkedlist import LinkedList
import sys


def determine_anagram(word, possible_anagram):
    """Determines if a word might be the anagram of another word.
       Credit for function comes from my CS 1.2 repo, can be found at
       https://github.com/UPstartDeveloper/CS-1.2-Intro-Data-Structures/blob/master/Code/anagram_app/app.py#L17

       Parameters:
       word(str)
       possible_anagram(str)

       Returns: bool

    """
    # cannot be an anagram if it's not same length
    if not len(word) == len(possible_anagram):
        return False
    # possible_anagram must be different from word
    if word == possible_anagram:
        return False
    # possible_anagram must have all same letters as word, in same distribution
    for letter in possible_anagram:
        if letter not in word:
            return False

    for letter in word:
        if letter not in possible_anagram:
            return False
    # all tests passed, then return True
    return True


def get_possible_words(jumbled_word):
    """Return the set of all words the same length as our input str.

        Parameters:
        jumbled_word(str): the str that represents a common English word, with
                           its letters misspelled. This str has the following
                           key characteristics:
                           - it is composed entirely of English letters
                           - letters may be repeated.
                           - all letters are lower case
                           - all letters will appear in correctly spelled word,
                             with the same distribution as in the input str

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
        [word for word in clean_words if determine_anagram(jumbled_word, word)]
    )


def unscramble(jumbled_word):
    """Returns a common English word, given a string that consists solely of
       English letters.

       Parameters:
       jumbled_word(str): the str that represents a common English word, with
                          its letters misspelled. This str has the following
                          key characteristics:
                          - it is composed entirely of English letters
                          - letters may be repeated.
                          - all letters are lower case
                          - all letters will appear in correctly spelled word,
                            with the same distribution as in the input str

        Returns:
        str: the unscrambled str

    """
    # create the set of all words that could be the real spelling
    possible_spellings_list = (
        get_possible_words(jumbled_word).collection.keys()
    )
    # dump all these words into a listr
    words = LinkedList(possible_spellings_list)
    # DEBUGGING: print all the words we came up with
    print(words)
    # return the first spelling
    if words.head is not None:
        return words.head.data
    else:
        return "Sorry, couldn't find a real English word."


if __name__ == "__main__":
    jumbled_word = sys.argv[1]
    print(unscramble(jumbled_word))
