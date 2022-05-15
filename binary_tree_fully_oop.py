## BINARY TREE - object oriented implementation

## according to Cambridge International

############################

class BinaryTree:
    SIZE = 10

    class Node:
        def __init__(self):
            self.data = ""
            self.left = None
            self.right = None

    def __init__(self):

        self.__nodes = [self.Node() for i in range(self.SIZE)]

        for i in range(self.SIZE - 1):
            self.__nodes[i].left = i + 1

        self.__free_pointer = 0
        self.__root_pointer = None

    ############################

    def find_insertion_point(self, new_data):

        pointer = self.__root_pointer

        while pointer is not None:
            prev_pointer = pointer
            current = self.__nodes[pointer].data

            if current < new_data:
                direction = "right"
                pointer = self.__nodes[pointer].right
            else:
                direction = "left"
                pointer = self.__nodes[pointer].left

        return prev_pointer, direction

    ############################

    def add(self, new_data):

        if self.__free_pointer is None:
            raise Exception("Error - tree is full")

        else:

            new_pointer = self.__free_pointer
            self.__nodes[new_pointer].data = new_data
            self.__free_pointer = self.__nodes[new_pointer].left
            self.__nodes[new_pointer].left = None

            if self.__root_pointer is None:
                self.__root_pointer = new_pointer
                print(f"Root pointer was set")
            else:
                pointer, direction = self.find_insertion_point(new_data)

                if direction == "left":
                    self.__nodes[pointer].left = new_pointer
                else:
                    self.__nodes[pointer].right = new_pointer

            print(f"Added {new_data} to the tree")

    ############################

    def search(self, data):

        pointer = self.__root_pointer
        search = True

        while search:
            current = self.__nodes[pointer].data

            if pointer is None:
                print(f"{data} was not found")
                search = False

            elif current == data:
                print(f"{data} was found at position {pointer}")
                search = False

            elif current < data:
                direction = "right"
                pointer = self.__nodes[pointer].right
            else:
                direction = "left"
                pointer = self.__nodes[pointer].left

    ############################

    def traverse(self, pointer=None):

        if self.__root_pointer is None:
            raise Exception("Cannot traverse, tree is empty")

        if pointer is None:
            pointer = self.__root_pointer

        left = self.__nodes[pointer].left
        right = self.__nodes[pointer].right
        data = self.__nodes[pointer].data

        if left is not None:
            self.traverse(left)

        print(data)

        if right is not None:
            self.traverse(right)

############################


def Test():
    print("\ntesting OOP binary tree\n")

    my_tree = BinaryTree()
    try:
        my_tree.traverse()
    except Exception as e:
        print(e)

    for animal in '''mouse
cat
dog
horse
sheep
goat
bat
lizard
lion
tiger
cheetah
giraffe'''.split("\n"):
        try:
            my_tree.add(animal)
        except Exception as e:
            print(e)

    print("Traversing tree...")

    my_tree.traverse()

############################
