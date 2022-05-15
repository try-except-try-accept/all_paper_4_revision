## BINARY TREE (unordered)

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

def AddToTree(NewData: str, AttachTo: str = None, Direction: str = None):
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
            Pointer, Found = SearchTree(AttachTo)
            if not Found:
                print(f"Error. Cannot attach to {AttachTo} - not found in tree")
                return

            if Direction == "Left":
                if Tree[Pointer].Left is None:
                    Tree[Pointer].Left = NewPointer
                else:
                    print(f"Cannot attach on the left. Already connected!")
                    return
            else:
                if Tree[Pointer].Right is None:
                    Tree[Pointer].Right = NewPointer
                else:
                    print(f"Cannot attach on the right. Already connected!")
                    return

            print(f"Attached {NewData} to the {Direction} of {AttachTo}")


############################

def SearchTree(FindData: str, Pointer: int = None, Found: bool = False) -> (int, bool):
    if Pointer is None:
        Pointer = RootPointer

    Left = Tree[Pointer].Left
    Right = Tree[Pointer].Right
    Data = Tree[Pointer].Data

    if Data == FindData:
        Found = True
    else:
        if Left is not None:
            Pointer, Found = SearchTree(FindData, Left)

        if Right is not None:
            Pointer, Found = SearchTree(FindData, Right)

    return Pointer, Found


############################

def TraverseTree(Pointer: int = None):
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

    print("\ntesting unordered binary tree\n")

    InitialiseTree()

    AddToTree("mouse")
    AddToTree("horse", "mouse", "Left")
    AddToTree("dog", "mouse", "Right")
    AddToTree("cat", "dog", "Left")
    AddToTree("sheep", "cat", "Left")
    AddToTree("lizard", "cat", "Right")
    AddToTree("lion", "sheep", "Left")
    AddToTree("tiger", "sheep", "Right")
    AddToTree("panda", "sheep", "Right")
    AddToTree("tiger", "elephant", "Right")
    TraverseTree()

############################
