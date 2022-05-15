## OOP Inheritance...

## According to Cambridge International

#########################################

## A cat has a favourite food, an age and a weight.

## A cat can meow its info.

## A cage stores up to 10 cats.

## A cage contains a clock and every 6 hours, all cats inside the cage meow.

# import the class to save rewriting the code
from oop_inheritance import Cat


class Cage:

    def __init__(self):

        # DECLARE Cats : ARRAY[0:9] OF Cat
        self.__Cats = [None for i in range(10)]  # use None as we don't know the instance params yet
        self.__Clock = 0
        self.__CatCount = 0

    def IncrementClock(self):
        self.__Clock += 1
        print("The time is", self.__Clock, ":00")
        if self.__Clock % 6 == 0:
            for i in range(self.__CatCount + 1):
                self.__Cats[i].Meow()

    def AddCat(self):
        Name = input("What's the name of the cat: ")
        Weight = input("How much does the cat weigh?: ")
        Age = input("How old is the cat?: ")
        i = self.__CatCount  # alias to make shorter lines

        self.__Cats[i] = Cat(Name, float(Weight), int(Age))
        self.__CatCount += 1


def Test():
    print("\ntesting oop containment\n")

    ThisCage = Cage()
    ThisCage.AddCat()
    ThisCage.AddCat()
    for i in range(13):
        ThisCage.IncrementClock()
