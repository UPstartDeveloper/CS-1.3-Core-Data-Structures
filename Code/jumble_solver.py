from set import Set
from linkedlist import LinkedList
from stack import Stack  # implements using LinkedStack
from hashtable import HashTable
import sys
from itertools import permutations

"""
def letter_distribution(word):
    '''Returns an associative array of a word, representing its letters and
       counts in the word.

       Parameter:
       word(str): a str composed of only English letters. All lower cases.

       Returns: HashTable

    '''
    histogram = HashTable()
    letters = histogram.keys()
    for letter in word:
        if letter not in letters:
            # add the intial entry of the letter into the hash table
            histogram.set(letter, 1)
            letters.append(letter)
        else:
            # increment the current letter count by one
            current_count = histogram.get(letter)
            histogram.set(letter, current_count + 1)
    return histogram


def compare_distributions(word_dist, possible_anagram_dist):
    '''Return True is all the letters in word appear in the same amount in the
       other word.

       Parameters:
       word_dist(HashTable): keys are letters, values are the number of times
                             that it appears in the word
       possible_anagram_dist(HashTable): structured same way as word_dist

       Returns: bool

    '''
    letters_in_word = word_dist.keys()
    letters_in_poss_anagram = possible_anagram_dist.keys()
    # for each letter in word, be sure it exists in the other word
    for letter in letters_in_word:
        if letter not in letters_in_poss_anagram:
            return False
        # also be sure that it appears the same number of times
        if not word_dist.get(letter) == possible_anagram_dist.get(letter):
            return False
    return True


def determine_anagram(word, possible_anagram):
    '''Determines if a word might be the anagram of another word.
       Credit for function comes from my CS 1.2 repo, can be found at
       https://github.com/UPstartDeveloper/CS-1.2-Intro-Data-Structures/blob/master/Code/anagram_app/app.py#L17

       Parameters:
       word(str)
       possible_anagram(str)

       Returns: bool

    '''
    # cannot be an anagram if it's not same length
    if not len(word) == len(possible_anagram):
        return False
    # make distributions of letters and counts of both str
    word_dist = letter_distribution(word)
    possible_anagram_dist = letter_distribution(possible_anagram)
    # check to make sure the letter distributions are the same, both ways
    word_dist_matches_possible = compare_distributions(word_dist,
                                                       possible_anagram_dist)
    possible_dist_matches_word = compare_distributions(possible_anagram_dist,
                                                       word_dist)
    # all tests passed, then return True
    return (
        word_dist_matches_possible is True and
        possible_dist_matches_word is True
    )


def unscramble(jumbled_word):
    '''Returns a common English word, given a string that consists solely of
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

    '''
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
"""

# Solution using permutations, Sets, and LinkedLists


def get_possible_words(length):
    '''Return the set of all words the same length as our input str.'''
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
    return Set([word for word in clean_words if len(word) == length])


def unscramble(word):
    '''Return intersection of all words, the set of all anagrams of word.'''
    # generate the set of all possible anagrams of the word
    anagrams = list(permutations(word))
    # convert this to a list of str, not tuple
    anagrams = [''.join(list(anagram)) for anagram in anagrams]
    # convert this to a Set
    anagrams = Set(anagrams)
    # generate the set of all English words in the dictionary file
    actual_words = get_possible_words(len(word))
    # find the intersection between the two
    overlap = anagrams.intersection(actual_words)
    # dump all the words into a LinkedList, and return the head
    unscrambled_words = LinkedList(word for word in overlap.collection.keys())
    if unscrambled_words.head is not None:
        print(unscrambled_words)  # shows all anagrams found
        return unscrambled_words.head.data
    else:
        return 'Sorry, no English word could be found.'


if __name__ == "__main__":
    jumbled_word = sys.argv[1]
    print(unscramble(jumbled_word))
