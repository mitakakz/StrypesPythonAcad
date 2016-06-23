from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        if not isinstance(node, Node):
            raise ValueError('node should be Node')

        self.children.append(node)


class Tree:
    def __init__(self, *, root):
        """
            When we are creating a new tree, we must always have a root element.
            For example:
            tree = Tree(root=5)
        """

        self.__root = Node(root)
        self.__found_by_value = None  # the Node containing the searched value


    def add(self, *, value, parent):
        """
            When we are adding new element to our tree, we must specify the parent:
            tree = Tree(root=5)
            tree.add(4, parent=5)
            tree.add(3, parent=5)
            tree.add(2, parent=4)

            This will make the following tree:

                5
               / \
              4   3
             /
            2
        """
        elem = Node(value)

        self.search(parent, self.__root)

        self.__found_by_value.add_child(elem)
        self.__found_by_value = None

    def search(self, x, vertex):
        if x == vertex.value:
            self.__found_by_value =  vertex
        #print(vertex.value)
        for child in vertex.children:
            self.search(x, child)

    def find(self, x):
        """
            Returns True or False if Node with value x is present in the tree
        """
        self.__found_by_value = None
        self.search(x, self.__root)
        if self.__found_by_value != None:
            return True
        else:
            return False

    def bfs_from_root(self):
        """
            Makes a Breadth-First-Search Algorithm from root
            Returns a list of tuples in the following format:
            [(tree_level, (node1_on_that_level, node2_on_that_level, ...)),
             (tree_level + 1, (node1_on_that_level, node2_on_that_level, ...))]

            If we take the tree from the add example, the result will look like that:

            [(1, (5, )),
             (2, (4, 3)),
             (3, (2, ))]

             We count our levels from 1.
        """
        pipe = deque()
        pipe.append(self.__root)
        result = []
        elems_per_level = ()
        level = 1
        lev_len = len(pipe)

        while True:
            elem = pipe.popleft()
            elems_per_level += (elem.value,)
            for p in elem.children:
                pipe.append(p)
            lev_len -= 1
            if lev_len == 0:
                result += [(level, elems_per_level)]
                level += 1
                elems_per_level = ()
                lev_len = len(pipe)
                if lev_len == 0:
                    break
        return result





tree = Tree(root=5)
tree.add(value=4,parent=5)
tree.add(value=3,parent=5)
tree.add(value=6,parent=3)
tree.add(value=7,parent=3)
print("__________________________________")
print(tree.find(4))
print(tree.bfs_from_root())
#tree.bfs_from_root()