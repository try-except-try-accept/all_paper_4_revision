## FILE PROCESSING - reading records from file

## According to Cambridge International


class Cat:

    def __init__(self, Name, Weight, Age):
        self.__Name = Name  # string
        self.__Weight = Weight  # real
        self.__Age = Age  # integer

    def Info(self):
        print(f'{self.__Name} weighs {self.__Weight} kg and is {self.__Age} years old.')


def ProcessFile(FileName: str) -> list:
    try:
        ## DECLARE Cats : ARRAY[0:2] OF Cat
        Cats = [None for i in range(3)]
        i = 0
        with open(FileName, "r") as File:
            Counter = 0
            for Line in File:
                Line = Line.strip()
                if Counter == 0:
                    Name = Line
                elif Counter == 1:
                    Weight = float(Line)
                else:
                    Age = int(Line)
                    Cats[i] = Cat(Name, Weight, Age)
                    i += 1

                Counter += 1
                if Counter == 3:
                    Counter = 0
    except FileNotFoundError:
        print(f"Could not find {FileName}")

    return Cats


def Test():
    print("\ntesting reading records from file\n")

    Cats = ProcessFile("cats.txt")

    for ThisCat in Cats:
        ThisCat.Info()
