

class Vector:

    """
    USAGE:
        - Fast indexing
        - unknown size of the data
    """
    def __init__(self):
        self.__capacity = 10
        self.__current_capacity = 0
        self.__storage =  [None]*self.__capacity

    def add_last(self, x):
        """Add last"""
        if self.__current_capacity > self.__capacity:
            self.__resize()

        self.__storage[self.__current_capacity] = x
        self.__current_capacity += 1

    def get(self, index):
        return self.__storage[index]

    def __resize(self):

        print("AHTUNG::::::RESIZING")
        new_capacity = self.__capacity*2+1
        new_storage = [None]*new_capacity

        for i in range(len(self.__storage)):
            new_storage[i] = self.__storage[i]
        self.__storage = new_storage
        self.__capacity = new_capacity

    def size(self):
        return len(self.__storage)

    def __len__(self):
        return self.__current_capacity


class Node:
    """From a linked list"""

    def __init__(self, value, next_node=None):
        self.value = value

        if next_node is not None and \
            not isinstance(next_node,Node):
            raise TypeError("next node should be an instance of Node")

        self.next_node = next_node

    def has_next(self):
        return self.next_node is not None


class DoubleLinkedList(Node):

    """All defs should have 0(1) complexity"""
    def __init__(self):
        pass

    def add_first(self, x):
        pass

    def add_last(self, x):
        pass

    def remove_first(self,x):
        pass

    def remove_last(self,x):
        pass

