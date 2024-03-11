import unittest


def is_substring(string: str, sub: str) -> bool:
    """
    -1 means method cannot find the index of the substring

    :param string:
    :param sub:
    :return:
    """
    return string.find(sub) != -1


def check_if_substring(string_1: str, string_2: str) -> bool:
    """
    Method to check if the second string is the rotation of the first string
    :param string_1:
    :param string_2:
    :return:
    """

    if len(string_1) != len(string_2):
        return False

    return is_substring(string_1 + string_1, string_2)


class TestClass(unittest.TestCase):

    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ("remi", "mire", True)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:

            self.assertEqual(
                check_if_substring(s1, s2),
                expected
            )


if __name__ == "__main__":
    unittest.main()
