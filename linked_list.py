class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Data --> {self.data}\nNext --> {self.next}'


class LinkedList:
    def __init__(self):
        self.head = Node(data=None)
        self.length = 0

    def __repr__(self):
        current = self.head
        str_repr = ''
        while current:
            if current.next:
                str_repr += f'{current.data} --> '
            else:
                str_repr += f'{current.data}'
            current = current.next
        return str_repr

    def __increment_length(self):
        self.length += 1

    def __decrement_length(self):
        self.length -= 1

    def __get_length(self):
        return self.length

    def __is_empty(self):
        if self.__get_length() == 0:
            return True
        else:
            return False

    def add(self, data):
        """
        Add element at end of linked-list
        :param data:
        :return: None
        """
        node = Node(data)

        if self.__is_empty():
            self.head = node
            self.__increment_length()
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.__increment_length()

    def add_at_beginning(self, data):
        """
        Add element at start of linked-list
        :param data:
        :return:
        """
        node = Node(data)
        if self.__is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
            self.__increment_length()

    def add_at_position(self, data, position):
        """
        Add element at given position of linked-list
        :param data:
        :param position:
        :return:
        """
        node = Node(data)
        if position < 0:
            raise ValueError(f'Input position {position} is not supported.')
        elif position == 0:
            self.add_at_beginning(data)
        # add inside linked-list
        elif position <= (self.__get_length() - 1):
            current = self.head
            for _ in range(position):
                previous = current
                current = current.next
            node.next = current
            previous.next = node
            self.__increment_length()
        # add at end
        else:
            self.add(data)

    def remove(self):
        """
        Removes element from beginning of list
        :return: Node
        """
        if self.__is_empty():
            return None
        else:
            node = Node(self.head.data)
            self.head = self.head.next
            self.__decrement_length()
            return node

    def remove_at_end(self):
        """
        Removes element from end of list
        :return: Node
        """
        if self.__is_empty():
            return None
        elif self.__get_length() == 1:
            node = Node(self.head.data)
            self.head.data = None
            self.__decrement_length()
            return node
        else:
            current = self.head
            while current.next:
                previous = current
                current = current.next
            node = Node(current.data)
            previous.next = None
            self.__decrement_length()
            return node

    def remove_at_position(self, position):
        """
        Removes element from specified position
        :param position:
        :return:
        """
        if position < 0:
            raise ValueError(f'Incorrect position {position}')
        elif position == 0:
            node = self.remove()
            return node
        elif position < (self.__get_length() - 1):
            current = self.head
            for _ in range(position):
                previous = current
                current = current.next
            node = Node(current.data)
            previous.next = current.next
            return node
        else:
            node = self.remove_at_end()
            return node
