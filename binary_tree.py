## BINARY TREE

## according to Cambridge International

############################

SIZE = 10


class Node:
    def __init__(self):
        self.Data = ""
        self.Left = None
        self.Right = None


############################

def InitialiseTree():
    global Tree, FreePointer, RootPointer

    Tree = [Node() for i in range(SIZE)]

    for i in range(SIZE - 1):
        Tree[i].Left = i + 1

    FreePointer = 0
    RootPointer = None


############################

def FindInsertionPoint(NewData: str) -> (int, str):
    Pointer = RootPointer

    while Pointer is not None:
        PrevPointer = Pointer
        Current = Tree[Pointer].Data

        if Current < NewData:
            Direction = "Right"
            Pointer = Tree[Pointer].Right
        else:
            Direction = "Left"
            Pointer = Tree[Pointer].Left

    return PrevPointer, Direction


############################

def AddToTree(NewData: str):
    global Tree, FreePointer, RootPointer

    if FreePointer is None:
        print("Error - tree is full")

    else:

        NewPointer = FreePointer
        Tree[NewPointer].Data = NewData
        FreePointer = Tree[NewPointer].Left
        Tree[NewPointer].Left = None

        if RootPointer is None:
            RootPointer = NewPointer
            print(f"Root pointer was set")
        else:
            Pointer, Direction = FindInsertionPoint(NewData)

            if Direction == "Left":
                Tree[Pointer].Left = NewPointer
            else:
                Tree[Pointer].Right = NewPointer

        print(f"Added {NewData} to the tree")


############################

def SearchTree(Data: str):
    Pointer = RootPointer
    Search = True

    while Search:
        Current = Tree[Pointer].Data

        if Pointer is None:
            print(f"{Data} was not found")
            Search = False

        elif Current == Data:
            print(f"{Data} was found at position {Pointer}")
            Search = False

        elif Current < Data:
            Direction = "Right"
            Pointer = Tree[Pointer].Right
        else:
            Direction = "Left"
            Pointer = Tree[Pointer].Left


############################

def TraverseTree(Pointer: int=None):
    if RootPointer is None:
        print("Cannot traverse, tree is empty")
        return

    if Pointer is None:
        Pointer = RootPointer

    Left = Tree[Pointer].Left
    Right = Tree[Pointer].Right
    Data = Tree[Pointer].Data

    if Left is not None:
        TraverseTree(Left)

    print(Data)

    if Right is not None:
        TraverseTree(Right)


############################

def Test():
    global Tree, FreePointer, RootPointer

    print("testing binary tree\n")

    InitialiseTree()

    for Animal in '''mouse
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
        AddToTree(Animal)

    TraverseTree()

############################
