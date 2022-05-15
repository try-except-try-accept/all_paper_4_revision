## QUEUE (circular)

## According to Cambridge International

############################

SIZE = 10


def Enqueue(NewData: str):
    global q, EndPointer

    if StartPointer == EndPointer and q[StartPointer] is not None:
        print("Queue is full")
    else:
        q[EndPointer] = NewData
        EndPointer += 1
        if EndPointer == SIZE:
            EndPointer = 0

        print(f"{NewData} was added to the queue")


############################

def Dequeue():
    global q, StartPointer

    if StartPointer == EndPointer and q[StartPointer] is None:
        print("Queue is empty")
    else:
        Removed = q[StartPointer]
        q[StartPointer] = None
        StartPointer += 1
        if StartPointer == SIZE:
            StartPointer = 0

        print(f"{Removed} left the queue")


############################

def CreateQueue():
    global q, StartPointer, EndPointer
    q = [None for i in range(SIZE)]  # ARRAY[0:9] OF STRING
    StartPointer = 0  # INTEGER / POINTER
    EndPointer = 0  # INTEGER / POINTER


############################

def Test():
    print("\ntesting queue\n")

    CreateQueue()

    Colours = '''yellow
blue
red
magenta
green
cyan
violet
aquamarine
pink
brown
grey
black'''.split("\n")

    for Col in Colours:
        Enqueue(Col)

    for i in range(10):
        Dequeue()

    Enqueue("yellow")
    Dequeue()
    Dequeue()
    Enqueue("red")
    Enqueue("blue")
    Dequeue()

############################
