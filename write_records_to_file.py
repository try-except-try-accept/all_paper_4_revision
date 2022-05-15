## FILE PROCESSING - reading records from file

## According to Cambridge International


class Cat:

    def __init__(self, Name, Weight, Age):
        self.__Name = Name
        self.__Weight = Weight
        self.__Age = Age

    def GetName(self) -> str:
        return self.__Name

    # return strings for ease of writing to file
    def GetWeight(self) -> str:
        return str(self.__Weight)

    def GetAge(self) -> str:
        return str(self.__Age)


def ProcessFile(Cats: list):
    with open("cats_new.txt", "a") as File:
        for ThisCat in Cats:
            File.write(ThisCat.GetName() + "\n")
            File.write(ThisCat.GetWeight() + "\n")
            File.write(ThisCat.GetAge() + "\n")


def GetCats() -> list:
    ## DECLARE Cats : ARRAY[0:2] OF Cat
    Cats = [None for i in range(3)]
    for i in range(3):
        Name = input("What's the name of the cat: ")
        Weight = input("How much does the cat weigh?: ")
        Age = input("How old is the cat?: ")

        Cats[i] = Cat(Name, float(Weight), int(Age))

    return Cats


def Test():
    print("\ntesting writing records to file\n")

    Cats = GetCats()
    ProcessFile(Cats)
