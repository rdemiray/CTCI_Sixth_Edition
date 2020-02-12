from Chapter_2.linked_list import LinkedList
import unittest


def remove_node_in_the_middle(middle_node):
    middle_node.data = middle_node.next.data
    middle_node.next = middle_node.next.next


class TestClass(unittest.TestCase):
    test_linked_list = LinkedList()
    test_linked_list.add(5)
    test_linked_list.add(10)
    middle_node_to_be_removed = test_linked_list.add(15)
    test_linked_list.add(20)
    test_linked_list.add(25)

    print("-------BEFORE--------")
    test_linked_list.print_all()

    print("-------AFTER--------")
    remove_node_in_the_middle(middle_node_to_be_removed)
    test_linked_list.print_all()


if __name__ == "__main__":
    unittest.main()

