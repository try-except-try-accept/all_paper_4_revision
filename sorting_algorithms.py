## BUBBLE SORT

#############

def BubbleEfficient(Arr: list) -> list:
    ## O(n²) worst case time complexity
    ## O(n-1) best case time complexity
    ## O(1/2n(n+1)) average case time complexity

    ## O(1) space complexity

    Max = len(Arr)

    Swap = True
    Pass = 1

    while Swap:
        Swap = False

        for j in range(Max - Pass):
            if Arr[j] > Arr[j + 1]:
                Temp = Arr[j]
                Arr[j] = Arr[j + 1]
                Arr[j + 1] = Temp
                Swap = True

        Pass += 1

    return Arr


#############

def BubbleInefficient(Arr: list) -> list:
    ## always O(n²) time complexity every time

    ## O(1) space complexity

    Max = len(Arr)

    for i in range(Max):
        for j in range(Max - 1):
            if Arr[j] > Arr[j + 1]:
                Temp = Arr[j]
                Arr[j] = Arr[j + 1]
                Arr[j + 1] = Temp

    return Arr


#############

def InsertionSort(Arr: list) -> list:
    ## O(n²) worst case time complexity
    ## O(n) best case time complexity
    ## O(n²) average case time complexity

    ## O(1) space complexity

    Max = len(Arr)
    for i in range(1, Max):
        InsertValue = Arr[i]
        InsertPos = i
        while InsertPos > 0 and Arr[InsertPos - 1] > InsertValue:
            Arr[InsertPos] = Arr[InsertPos - 1]
            InsertPos -= 1
        Arr[InsertPos] = InsertValue


#############

def Test():
    from random import randint
    from timeit import timeit
    Data = [randint(1000, 9999) for i in range(100)]
    print("\nTesting inefficient bubble sort\n")
    Before = timeit()
    BubbleInefficient(list(Data))
    print(f"Sorted 1000 integers in {timeit() - Before}")
    print("\nTesting efficient bubble sort\n")
    Before = timeit()
    BubbleEfficient(list(Data))
    print(f"Sorted 1000 integers in {timeit() - Before}")
    print("\nTesting insertion sort\n")
    Before = timeit()
    InsertionSort(list(Data))
    print(f"Sorted 1000 integers in {timeit() - Before}")
