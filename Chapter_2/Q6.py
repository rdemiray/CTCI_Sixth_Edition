from Chapter_2.linked_list import LinkedList
import unittest


def check_if_palindrome(given_linked_list):
    """
    Assumption is that Linked list is Singly linked list
    :param given_linked_list:
    :return:
    """
    # Iterate over the linked list and covert it into a list and then process list

    current_node = given_linked_list.head
    ll_elements = []

    while current_node:
        ll_elements.append(current_node.data)
        current_node = current_node.next

    pointer_1 = 0
    pointer_2 = len(ll_elements) - 1

    while pointer_1 < pointer_2:
        if ll_elements[pointer_1] != ll_elements[pointer_2]:
            return False
        else:
            pointer_1 += 1
            pointer_2 -= 1

    return True


def check_if_palindrome_doubly_linked_list(given_linked_list):
    """
    Input Linked list is doubly linked.....
    Use two cursors and move one forward the other backward.....
    :param given_linked_list:
    :return:
    """
    # TODO: Missing implementation
    pass


class TestClass(unittest.TestCase):
    test_linked_list = LinkedList()
    test_linked_list.add("a")
    test_linked_list.add("b")
    test_linked_list.add("c")
    test_linked_list.add("b")
    test_linked_list.add("a")

    check_if_palindrome(test_linked_list)
    # TODO: Missing test implementation
