## LINKED LIST
## According to Cambridge International

SIZE = 10


class Node:
    def __init__(self):
        self.Data = ""
        self.Pointer = None


def CreateList():
    global List, HeadPointer, FreePointer

    List = [Node() for i in range(SIZE)]

    for i in range(SIZE - 1):
        List[i].Pointer = i + 1

    FreePointer = 0
    HeadPointer = None


##############

def Insert(NewData: str):
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
            Pointer = HeadPointer
            LastPointer = None
            Current = List[Pointer].Data
            InsertFound = False

            while not InsertFound:
                if NewData < Current:
                    InsertFound = True
                else:
                    LastPointer = Pointer
                    Pointer = List[Pointer].Pointer
                    if Pointer is not None:
                        Current = List[Pointer].Data
                    else:
                        InsertFound = True

            if LastPointer is not None:
                List[LastPointer].Pointer = NewPointer
            else:
                HeadPointer = NewPointer

            List[NewPointer].Pointer = Pointer

            print(f"Inserted {NewData}  in the list.")


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
    print("\ntesting ordered linked list\n")

    CreateList()
    Insert("mozambique")
    DisplayList()
    Insert("argentina")
    DisplayList()
    Insert("moldova")
    DisplayList()
    Insert("iceland")
    DisplayList()
    Insert("burkina faso")
    DisplayList()
    Insert("nigeria")
    DisplayList()
    Insert("malaysia")
    Insert("laos")
    DisplayList()
    Delete("argentina")
    DisplayList()
    Delete("mozambique")
    DisplayList()
    Delete("england")
    DisplayList()
    Insert("england")
    DisplayList()
