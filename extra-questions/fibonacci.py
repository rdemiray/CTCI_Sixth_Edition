import unittest

"""
Fibonacci Numbers:

    F(n) = F(n-1) + F(n-2)
    F(0) = 0
    F(1) = 1

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""


def fibonacci_recursive(n):
    """
    Method to return n'th Fibonacci number using recursive approach
    """

    if n < 0:
        raise ValueError('Input must be non-negative integer')
    
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    """
    Method to return n'th Fibonacci number using iterative approach

    """

    if n < 0:
        raise ValueError('Input must be non-negative integer')
    
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    a = 0
    b = 1

    for _ in range(2, n+1):
        # Simultaneous update, Python evaluates the right-hand side first
        a, b = b, a + b

    return b 





    

class TestClass(unittest.TestCase):

    test_data = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34)
    ]

    def test_method(self):

        for data in self.test_data:
            self.assertEqual(fibonacci_recursive(data[0]), data[1])
            self.assertEqual(fibonacci_iterative(data[0]), data[1])


if __name__ == "__main__":
    unittest.main()