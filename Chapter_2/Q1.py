
# Trial commit to Github

from Chapter_2.linked_list import LinkedList
import unittest


def remove_duplicates(given_linked_list):

    if given_linked_list.head is None:
        print("Linked List is empty... There is nothing to remove")
        return

    current_node = given_linked_list.head
    previous_node = None

    # Create an empty list
    dups_removed = []

    while current_node:
        if current_node.data not in dups_removed:
            dups_removed.append(current_node.data)
            previous_node = current_node
            current_node = current_node.next
        else:
            # This element has been seen before... So needs to be deleted from the linked list
            previous_node.next = current_node.next
            current_node = current_node.next

    return given_linked_list


class TestClass(unittest.TestCase):

    test_linked_list = LinkedList()
    test_linked_list.add(5)
    test_linked_list.add(10)
    test_linked_list.add(15)
    test_linked_list.add(15)
    test_linked_list.add(25)
    test_linked_list.add(10)
    test_linked_list.add(10)
    test_linked_list.add(30)

    expected_linked_list = LinkedList()
    expected_linked_list.add(5)
    expected_linked_list.add(10)
    expected_linked_list.add(15)
    expected_linked_list.add(25)
    expected_linked_list.add(30)

    print("-------BEFORE--------")
    test_linked_list.print_all()

    unique_ll = remove_duplicates(test_linked_list)
    print("-------AFTER--------")
    unique_ll.print_all()
    print("-----EXPECTED-------")
    expected_linked_list.print_all()

    # def test_method(self):
    #     unique_ll = remove_duplicates(self.test_linked_list)
    #     current_expected_node = self.expected_linked_list.head
    #     current_actual_node = self.unique_ll.head
    #
    #     while current_expected_node is not None:
    #         self.assertEqual(current_expected_node.data, current_actual_node.data)
    #         current_expected_node = current_expected_node.next
    #         current_actual_node = current_actual_node.next


if __name__ == "__main__":
    unittest.main()








