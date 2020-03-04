from set import Set
from linkedlist import LinkedList
from stack import Stack  # implements using LinkedStack
from hashtable import HashTable
import sys
from itertools import permutations

# Solution using permutations, Sets, and LinkedLists


def get_possible_words(length):
    '''Return the set of all words the same length as our input str.'''
    # get words from the words file
    file = open("/usr/share/dict/words", "r")
    words_list = file.read().split("\n")
    file.close()
    # return the set of all words with the appropiate length
    return Set([word for word in words_list if len(word) == length])


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
