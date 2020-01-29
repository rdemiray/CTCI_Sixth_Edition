class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next(self):
        return self.next
        
    def set_next(self, val):
        self.next = val


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None

    def add(self, item):
        """
        Add the item to the list
        :param item:
        :return:
        """
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """
        Return the length/size of the list
        :return:
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        """
        Search for item in list. If found, return True. If not found, return False
        :param item:
        :return:
        """

        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() is item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        """

        :param item:
        :return:
        """
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() is item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if found:
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
        else:
            raise ValueError
            print('Value not found.')

    def insert(self, position, item):
        """
        Insert item at position specified. If position specified is
        out of bounds, raise IndexError
        :param position:
        :param item:
        :return:
        """

        if position > self.size() - 1:
            raise IndexError
            print("Index out of bounds.")
        current = self.head
        previous = None
        pos = 0
        if position is 0:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.get_next()
            previous.set_next(new_node)
            new_node.set_next(current)

    def index(self, item):
        """
        Return the index where item is found.
        If item is not found, return None.
        :param item:
        :return:
        """

        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.get_data() is item:
                found = True
            else:
                current = current.get_next()
                pos += 1
        if found:
            pass
        else:
            pos = None

        return pos

    def pop(self, position = None):
        """
        If no argument is provided, return and remove the item at the head.
        If position is provided, return and remove the item at that position.
        If index is out of bounds, raise IndexError
        :param position:
        :return:
        """

        if position > self.size():
            print('Index out of bounds')
            raise IndexError
        current = self.head
        if position is None:
            ret = current.get_data()
            self.head = current.get_next()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.get_next()
                pos += 1
                ret = current.get_data()
            previous.set_next(current.get_next())
        print(ret)
        return ret

    def append(self, item):
        """
        Append item to the end of the list
        :param item:
        :return:
        """
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.get_next()
            pos += 1
        new_node = Node(item)
        if previous is None:
            new_node.set_next(current)
            self.head = new_node
        else:
            previous.set_next(new_node)

    def print_list(self):
        """
        Print the list
        :return:
        """

        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()


ll = LinkedList()
ll.add('l')
ll.add('H')
ll.insert(1, 'e')
ll.append('l')
ll.append('o')
ll.print_list()
