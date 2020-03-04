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
        return unscrambled_words.head.data
    else:
        return 'Sorry, no English word could be found.'


def solve_jumble(list_of_jumbled):
    '''Solves the whole jumble given a list of words that need unscrambling.'''
    # define a dictionary that will store information related to each word
    scrambled_unscrambled = HashTable(len(list_of_jumbled))
    # store unscrambled version of all word in a list
    list_of_unjumbled = [unscramble(word) for word in list_of_jumbled]
    # store indices we're interested in at each solved word
    letters_of_interest = [
        list_of_unjumbled[0][2] + list_of_unjumbled[0][4],
        (list_of_unjumbled[1][0] + list_of_unjumbled[1][1] +
         list_of_unjumbled[1][3]),
        list_of_unjumbled[2][5],
        list_of_unjumbled[3][3] + list_of_unjumbled[3][4],
    ]
    # return the final result of the jumble
    answer = ''
    for piece in letters_of_interest:
        answer += piece
    return answer


if __name__ == "__main__":
    # Solving the first four words of the jumble
    scrambled_unscrambled = HashTable(4)
    jumbled = [
        'tefon',
        'sokik',
        'niumem',
        'siconu'
    ]
    print(f'The answer to the jumble is: {solve_jumble(jumbled)}')
