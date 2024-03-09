"""
Do the following if you get error on MAC (This is kind of a pre-requisite to run PyEnchant module on MAC)
ImportError: The 'enchant' C library was not found and maybe needs to be installed.


brew update
brew install enchant

"""
from itertools import permutations
import enchant
import sys


def find_eng_words(letters, word_length):
    """
    Ex. find_eng_words("LONLEP", 3)

    :param letters: [string]
    :param word_length: [int]
    :return: Does not return anything. Prints out output to console
    """
    word_length = int(word_length)
    letters = str(letters)
    print("Argument 1: {}".format(letters))
    print("Argument 2: {}".format(word_length))
    en_dict = enchant.Dict("en_US")

    all_permutations = list(permutations(letters, word_length))
    list_of_all_words = []

    for item in all_permutations:
        new_data = list(' '.join(w) for w in item)
        comb = "".join(new_data)
        # Make sure the uniqueness of each word. Don't print out repeating words
        if en_dict.check(comb) and comb not in list_of_all_words:
            list_of_all_words.append(comb)
            print(comb)


if __name__ == "__main__":
    """
    E.g. "python3 name_of_the_file.py ARG1 ARG2", if you'd like to run the file directly from command line
    python3 word_game_solver.py "LONLEP" 3
    """
    find_eng_words(sys.argv[1], sys.argv[2])





