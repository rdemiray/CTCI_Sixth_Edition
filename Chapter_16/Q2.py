"""
Freq of occurrences of any given word in a book.

Here is a little book :

"    Once upon a time there was this book.
This is a sentence. This is a much longer sentence.
This book is terribly short. But you get the idea.
You should see the word this 6 times in this example text.    "

"""

import unittest
import string


def remove_punctuations(given_string: str) -> str:
    """

    :param given_string:
    :return:
    """
    resultant_string = given_string.translate(str.maketrans('', '', string.punctuation))
    return resultant_string


def find_word_frequency_in_a_book(book: str, word:str) -> int:
    """
    Assumptions:
        - Book will be given in string form. A very long string naturally with punctuation marks
        - Word will be given in string from with either lower or upper case


    :param book:
    :param word:
    :return:
    """

    # Remove punctuations from the book and make it lower case
    processed_book = remove_punctuations(book).lower()
    processed_book = processed_book.split()

    word = word.lower()

    word_freq = 0

    for item in processed_book:
        if item == word:
            word_freq += 1

    return word_freq


class TestClass(unittest.TestCase):

    test_data = [
        (
            "    Once upon a time there was this book.!!! "
            "This is a sentence. This is a much longer sentence.??? "
            "This book is terribly short. But you get the idea.$$$ "
            "You should see the word this 6 times in this example text@#$%^&*()-=_.    ",
            "this",
            6
        ),
        (
            "    Once upon a time there was this book.!!! "
            "This is a sentence. This is a much longer sentence.??? "
            "This book is terribly short. But you get the idea.$$$ "
            "You should see the word this 6 times in this example text@#$%^&*()-=_.    ",
            "ThiS",
            6
        ),
    ]

    def test_method(self):

        for data in self.test_data:
            self.assertEqual(
                find_word_frequency_in_a_book(data[0], data[1]),
                data[2]
            )


if __name__ == "__main__":
    unittest.main()
