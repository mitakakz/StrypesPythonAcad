

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


class Linked_list:
    """From a linked list"""

    def __init__(self, value, next_node=None):
        self.value = value



        self.next_node = next_node

    def has_next(self):
        return self.next_node is not None

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value

        if next is not None and\
                not isinstance(next, Node):
            raise TypeError('next should be instance of Node')

        if prev is not None and\
                not isinstance(prev, Node):
            raise TypeError('prev should be instance of Node')

        self.prev = prev
        self.next = next

    def has_prev(self):
        return self.prev is not None

    def has_next(self):
        return self.next is not None

    def __str__(self):
        return "{}<-{}->{}".format(self.prev, self.value, self.next)


class DoublyLinkedList():
    def __init__(self):
        self.head_point = None
        self.tail_point = None
        self.count = 0


    """ O(1) - Returns a Node object that represents the head """
    def get_head(self):
        return self.head_point


    """ O(1) - Returns a Node object that represents the head """
    def get_tail(self):
        return  self.tail_point

    """ O(1) - Returns the value of the first element """
    def get_first(self):
        return self.head_point.value

    """ O(1) - Returns the value of the last element """
    def get_last(self):
        if self.tail_point != None:
            return self.tail_point.value
        else:
            return None

    """ O(1) """
    def add_first(self, x):
        elem = Node(x)
        if self.head_point != None:
            self.head_point.prev = elem
            elem.next = self.head_point
        self.head_point = elem
        if self.tail_point == None:
            self.tail_point = elem
        self.count += 1


    """ O(1) """
    def add_last(self, x):
        elem = Node(x)
        if self.tail_point != None:
            self.tail_point.next = elem
            elem.prev = self.tail_point
        self.tail_point = elem
        if self.head_point == None:
            self.head_point = elem
        self.count += 1

    """ O(1) """
    def remove_first(self):
        if self.head_point == self.tail_point:
            self.tail_point = None
        if self.head_point != None:
            val = self.head_point.value
            self.head_point = self.head_point.next
        if self.head_point != None:
            self.head_point.prev = None
        self.count -= 1
        return val

    """ O(1) """
    def remove_last(self):
        if self.head_point == self.tail_point:
            self.head_point = None

        if self.tail_point != None:
            val = self.tail_point.value
            self.tail_point = self.tail_point.prev

        if self.tail_point != None:
            self.tail_point.next = None
        if self.count > 0:
            self.count -= 1
            return val
        else: return None

    """ O(1) """
    def __len__(self):
        return self.count

    """ O(n) - Called when we do list(items) """
    def __iter__(self):
        result = []
        node = self.head_point
        while node != None:
            result.append(node.value)
            node = node.next
        return iter(result)

class Stack():

    def __init__(self):
        self.__dll = DoublyLinkedList()
        self.result = True
    def push(self, x):
        self.__dll.add_last(x)
        self.result = True

    def pop(self):
        val = self.__dll.get_last()
        self.__dll.remove_last()
        if val != None:
            return val


    def get_depth(self):
        return self.__dll.count



open = Stack()
close = Stack()

for el in "((()))":
    if el == "(":
        open.push(1)
    if el == ")":
        close.push(1)
print(open.get_depth(), close.get_depth())

if open.get_depth() == close.get_depth():
    print("True")
else:
    print("False")

"""
for el in "(()))":
    if el == "(":
         print(braces.gqet_depth())
    if el == ")":
        braces.pop()
        print(braces.get_depth())
print(braces.get_depth())
if braces.get_depth() ==0 :
    print("True")
else:
    print("False")


"""



"""
items = DoublyLinkedList()
items.add_first(5)
items.add_first(6)

assert items.get_first()==6
assert items.get_last()==5
assert len(items) == 2
assert list(items) == [6,5]

assert items.remove_first() == 6
assert len(items) == 1
assert items.remove_first() == 5
"""

