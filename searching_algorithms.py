## SEARCHING ALGORITHMS

#############

# Info on Big O : https://www.upgrad.com/blog/binary-search-algorithm/#:~:text=The%20time%20complexity%20of%20the,directly%20match%20the%20desired%20value.

def LinearSearch(Arr: list, Item: int) -> int:
    ## best case time complexity is O(1)
    ## worst case time complexity is O(n)
    ## average case time complexity is O(n/2)

    i = 0
    Found = False
    while i < len(Arr) and not Found:

        if Arr[i] == Item:
            Found = True
        else:
            i += 1

    if Found:
        return i
    else:
        return -1


#############

def BinarySearch(Arr: list, Item: int) -> int:
    ## best case time complexity is O(1)
    ## worst case time complexity is O(log n).
    ## average case time complexity is O(log n).

    ## iterative version has O(1) space complexity

    Left = 0
    Right = len(Arr)
    Found = False
    while Left < Right and not Found:
        Mid = (Left + Right) // 2

        if Arr[Mid] == Item:
            Found = True
        elif Arr[Mid] < Item:
            Left = Mid + 1
        else:
            Right = Mid - 1

    if Found:
        return Mid
    else:
        return -1


#############

def RecursiveBinarySearch(Arr: list, Item: int,
                          Left: int = 0, Right: int = None) -> int:
    ## best case time complexity is O(1)
    ## worst case time complexity is O(log n).
    ## average case time complexity is O(log n).

    ## recursive version has  O(log n) space complexity

    if Right is None:
        Right = len(Arr)

    if Left >= Right:
        return -1

    Mid = (Left + Right) // 2

    if Arr[Mid] == Item:
        Found = True
    elif Arr[Mid] < Item:
        return RecursiveBinarySearch(Arr, Item, Mid + 1, Right)
    else:
        return RecursiveBinarySearch(Arr, Item, Left, Mid - 1)

    return Mid


#############

def Test():
    Arr = [i for i in range(100)]

    print("\nTesting linear search\n")

    TestCases = [0, 1, 57, 99, 100, -4]
    for MyTest in TestCases:
        print(f"Searching for {MyTest}:", LinearSearch(Arr, MyTest))

    print("\nTesting binary search\n")
    for MyTest in TestCases:
        print(f"Searching for {MyTest}:", BinarySearch(Arr, MyTest))

    print("\nTesting recursive binary search\n")
    for MyTest in TestCases:
        print(f"Searching for {MyTest}:", RecursiveBinarySearch(Arr, MyTest))
