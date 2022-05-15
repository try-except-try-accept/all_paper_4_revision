## LINKED LIST

## According to Cambridge International


SIZE = 10


class Node:
    def __init__(self):  # comment
        self.Data = ""  # comment
        self.Pointer = None  # comment


def CreateList():
    global List, HeadPointer, FreePointer

    List = [Node() for i in range(SIZE)]

    for i in range(SIZE - 1):
        List[i].Pointer = i + 1

    FreePointer = 0
    HeadPointer = None


##############

def Append(NewData: str):
    global List, HeadPointer, FreePointer

    if FreePointer is None:
        print(f"List is full. Cannot add {NewData}")

    else:

        NewPointer = FreePointer
        FreePointer = List[NewPointer].Pointer
        List[NewPointer].Data = NewData
        List[NewPointer].Pointer = None

        # find the end of the list

        if HeadPointer is None:
            HeadPointer = NewPointer

        else:

            Pointer = HeadPointer

            while Pointer is not None:
                LastPointer = Pointer
                Pointer = List[Pointer].Pointer

            List[LastPointer].Pointer = NewPointer

        print(f"Appended {NewData} to the list.")


##############

def Prepend(NewData: str):
    global List, HeadPointer, FreePointer

    if FreePointer is None:
        print(f"List is full. Cannot add {NewData}")

    else:

        NewPointer = FreePointer
        FreePointer = List[NewPointer].Pointer
        List[NewPointer].Data = NewData
        List[NewPointer].Pointer = None

        if HeadPointer is None:
            HeadPointer = NewPointer

        else:

            List[NewPointer].Pointer = HeadPointer
            HeadPointer = NewPointer

        print(f"Prepended {NewData} to the list.")


##############

def Insert(NewData: str, After: str):
    global List, HeadPointer, FreePointer

    if FreePointer is None:
        print(f"List is full. Cannot add {NewData}")

    else:

        if HeadPointer is None:
            print("Cannot insert after {After}. List is empty.")
        else:
            NewPointer = FreePointer

            # if After exists in the list, insert the new item
            Pointer = HeadPointer
            Search = True

            while Search:

                Current = List[Pointer].Data
                if Current == After:
                    Search = False

                else:
                    Pointer = List[Pointer].Pointer
                    if Pointer is None:
                        Search = False

            if Pointer is None:
                print("Cannot insert. {After} was not found.")
            else:
                FreePointer = List[NewPointer].Pointer
                List[NewPointer].Data = NewData
                NextPointer = List[Pointer].Pointer
                List[Pointer].Pointer = NewPointer
                List[NewPointer].Pointer = NextPointer

                print(f"Inserted {NewData} after {After} in the list.")


##############

def Delete(DeleteData: str):
    global List, HeadPointer, FreePointer

    if HeadPointer is None:
        print("Nothing to delete. List is empty")

    else:

        Pointer = HeadPointer

        Search = True
        NotFound = False
        LastPointer = None

        while Search:

            Current = List[Pointer].Data
            if Current == DeleteData:
                Search = False

            else:
                LastPointer = Pointer
                Pointer = List[Pointer].Pointer
                if Pointer is None:
                    Search = False
                    NotFound = True

        if NotFound:
            print(f"Cannot delete {DeleteData}, not found in list")
        else:
            DeletePointer = Pointer
            NextPointer = List[DeletePointer].Pointer
            if LastPointer is None:  # deleting the head node
                HeadPointer = NextPointer
            else:
                List[LastPointer].Pointer = NextPointer
            List[DeletePointer].Data = ""
            List[DeletePointer].Pointer = FreePointer
            FreePointer = DeletePointer

            print(f"Deleted {DeleteData}")


##############

def DisplayList():
    Pointer = HeadPointer

    while Pointer is not None:
        print(List[Pointer].Data, end=", ")
        Pointer = List[Pointer].Pointer

    print()


##############

def Test():
    print("\ntesting linked list\n")

    CreateList()
    Append("mozambique")
    DisplayList()
    Prepend("argentina")
    DisplayList()
    Append("moldova")
    DisplayList()
    Prepend("iceland")
    DisplayList()
    Prepend("burkina faso")
    DisplayList()
    Prepend("nigeria")
    DisplayList()
    Prepend("malaysia")
    Insert("laos", "iceland")
    DisplayList()
    Delete("argentina")
    DisplayList()
    Delete("mozambique")
    DisplayList()
    Delete("england")
    DisplayList()
    Insert("england", "moldova")
    DisplayList()
