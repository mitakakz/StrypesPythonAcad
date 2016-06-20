

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



        self.next_node = next_node

    def has_next(self):
        return self.next_node is not None


class DoubleLinkedList(Node):

    """All defs should have 0(1) complexity"""
    def __init__(self,value, next_node=None, prev_node=None):
        self.prev = prev_node

        if (next_node is not None or prev_node is not None) and \
                (not isinstance(next_node, Node) or not isinstance(next_node, DoubleLinkedList)):
            raise TypeError("next node should be an instance of Node or DoubleLinkedList")

        super().__init__(value,next_node)

    def __str__(self):
        return str(self.value)

    def add_first(self, head):
        self.next_node = head
        head.prev = self

    def add_last(self, tail):
        self.prev = tail
        tail.next_node = self

    def remove_first(self):
        self.next_node.prev = None

    def remove_last(self,x):
        self.prev.next_node = None

    def print_list(self):
        obj = self
        while True :

            print(obj)
            if obj.next_node == None:
                break
            obj = obj.next_node


a = DoubleLinkedList(2)
c = DoubleLinkedList(4)
b = DoubleLinkedList(3,c,a)
a.add_first(b)
h = DoubleLinkedList(1)
h.add_first(a)
c.add_last(b)


h.print_list()