from itertools import permutations
import enchant
import sys


def find_eng_words(letters, word_length):
    word_length = int(word_length)
    letters = str(letters)
    print("Argument 1: {}".format(letters))
    print("Argument 2: {}".format(word_length))
    en_dict = enchant.Dict("en_US")

    all_permutations = list(permutations(letters, word_length))

    for item in all_permutations:
        new_data = list(' '.join(w) for w in item)
        comb = "".join(new_data)
        if en_dict.check(comb):
            print(comb)

# find_eng_words("LONLEP", 3)


if __name__ == "__main__":
    find_eng_words(sys.argv[1], sys.argv[2])





