"""
Write a Python program such that if an element in MxN matrix is zero, its entire row and column are set to zero

matrix = [
 [1,2,3,4],
 [5,6,7,8],
 [9,10,11,12]
]
"""
import copy
import unittest


def zeroize_matrix(matrix):
    """

    :param matrix:
    :return:
    """

    num_of_columns = len(matrix[0])
    num_of_rows = len(matrix)

    rows_to_zeroize = []
    cols_to_zeroize = []

    # Iterate over each row and column and identify columns and rows to zeroize in each iteration

    for row_index in range(num_of_rows):
        for col_index in range(num_of_columns):
            if matrix[row_index][col_index] == 0:
                rows_to_zeroize.append(row_index)
                cols_to_zeroize.append(col_index)

    # Now that we collected which rows and cols to zeroize, we can actually zeroize them

    for row_num in rows_to_zeroize:
        matrix = zeroize_row(matrix, row_num)

    for col_num in cols_to_zeroize:
        matrix = zeroize_column(matrix, col_num)

    return matrix


def zeroize_column(matrix, column_num):
    """

    :param matrix:
    :param column_num:
    :return:
    """
    num_of_rows = len(matrix)

    for row in range(num_of_rows):
        matrix[row][column_num] = 0

    return matrix


def zeroize_row(matrix, row_num):
    """

    :param matrix:
    :param row_num:
    :return:
    """
    num_of_cols = len(matrix[0])

    for i in range(num_of_cols):
        matrix[row_num][i] = 0

    return matrix


class TestClass(unittest.TestCase):
    test_data_1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    expected_test_data_1 = [
        [1, 2, 3, 4],
        [0, 0, 0, 0],
        [9, 10, 11, 12]
    ]

    expected_test_data_2 = [
        [0, 0, 0, 0],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    expected_test_data_3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0, 0, 0, 0],
    ]

    expected_test_data_4 = [
        [1, 2, 0, 4],
        [5, 6, 0, 8],
        [9, 10, 0, 12]
    ]

    input_test_matrix = [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
    ]

    expected_test_matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
    ]


    def test_method_zeroize_row_1(self):
        test_data = copy.deepcopy(self.test_data_1)
        self.assertEqual(
            zeroize_row(test_data, 1),
            self.expected_test_data_1
        )

    def test_method_zeroize_row_2(self):
        test_data = copy.deepcopy(self.test_data_1)
        self.assertEqual(
            zeroize_row(test_data, 0),
            self.expected_test_data_2
        )

    def test_method_zeroize_row_3(self):
        test_data = copy.deepcopy(self.test_data_1)
        self.assertEqual(
            zeroize_row(test_data, 2),
            self.expected_test_data_3
        )

    def test_method_zeroize_col(self):
        test_data = copy.deepcopy(self.test_data_1)
        self.assertEqual(
            zeroize_column(test_data, 2),
            self.expected_test_data_4
        )

    def test_zeroize_matrix(self):
        test_data = copy.deepcopy(self.input_test_matrix)

        self.assertEqual(
            zeroize_matrix(test_data),
            self.expected_test_matrix
        )


if __name__ == "__main__":
    unittest.main()
