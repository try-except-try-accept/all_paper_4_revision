## LINKED LIST (using a 2D array)

## According to Cambridge International


SIZE = 10


def CreateList():
    global List, HeadPointer, FreePointer

    List = [["", None] for i in range(SIZE)]

    for i in range(SIZE - 1):
        List[i][1] = i + 1

    FreePointer = 0
    HeadPointer = None


##############

def Append(NewData: str):
    global List, HeadPointer, FreePointer

    if FreePointer is None:
        print(f"List is full. Cannot add {NewData}")

    else:

        NewPointer = FreePointer
        FreePointer = List[NewPointer][1]
        List[NewPointer][0] = NewData
        List[NewPointer][1] = None

        # find the end of the list

        if HeadPointer is None:
            HeadPointer = NewPointer

        else:

            Pointer = HeadPointer

            while Pointer is not None:
                LastPointer = Pointer
                Pointer = List[Pointer][1]

            List[LastPointer][1] = NewPointer

        print(f"Appended {NewData} to the list.")


##############

def Prepend(NewData: str):
    global List, HeadPointer, FreePointer

    if FreePointer is None:
        print(f"List is full. Cannot add {NewData}")

    else:

        NewPointer = FreePointer
        FreePointer = List[NewPointer][1]
        List[NewPointer][0] = NewData
        List[NewPointer][1] = None

        if HeadPointer is None:
            HeadPointer = NewPointer

        else:

            List[NewPointer][1] = HeadPointer
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

                Current = List[Pointer][0]

                if Current == After:
                    Search = False

                else:
                    # LastPointer = Pointer
                    Pointer = List[Pointer][1]
                    if Pointer is None:
                        Search = False

            if Pointer is None:
                print("Cannot insert. {After} was not found.")
            else:
                FreePointer = List[NewPointer][1]
                List[NewPointer][0] = NewData
                NextPointer = List[Pointer][1]
                List[Pointer][1] = NewPointer
                List[NewPointer][1] = NextPointer

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

            Current = List[Pointer][0]
            if Current == DeleteData:
                Search = False

            else:
                LastPointer = Pointer
                Pointer = List[Pointer][1]
                if Pointer is None:
                    Search = False
                    NotFound = True

        if NotFound:
            print(f"Cannot delete {DeleteData}, not found in list")
        else:
            DeletePointer = Pointer
            NextPointer = List[DeletePointer][1]
            if LastPointer is None:  # deleting the head node
                HeadPointer = NextPointer
            else:
                List[LastPointer][1] = NextPointer
            List[DeletePointer][0] = ""
            List[DeletePointer][1] = FreePointer
            FreePointer = DeletePointer


##############

def DisplayList():
    Pointer = HeadPointer

    while Pointer is not None:
        print(List[Pointer][0], end=", ")
        Pointer = List[Pointer][1]

    print()


##############

def Test():
    print("\ntesting linked list w/ 2d array\n")

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
    Prepend("nigeria")
    Prepend("malaysia")
