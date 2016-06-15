

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