## OOP Inheritance...

## According to Cambridge International

#########################################

## A cat has a favourite food, an age and a weight.

## A cat can meow its info.

## A tiger is a cat who also has a number of stripes.

## A tiger can "ROAR" its info by repeating its meow once for every stripe it has.


class Cat:

    def __init__(self, Name, Weight, Age):
        self.__Name = Name  # string
        self.__Weight = Weight  # real
        self.__Age = Age  # integer

    def GetName(self) -> str:
        return self.__Name

    def GetWeight(self) -> float:
        return self.__Weight

    def GetAge(self) -> int:
        return self.__Age

    def SetName(self, NewName: str):
        self.__Name = NewName

    def SetWeight(self, NewWeight: float):
        self.__Weight = NewWeight

    def SetAge(self, NewAge: int):
        self.__Age = NewAge

    def Meow(self):
        ## it's necessary to use getters here as this method will be inherited into a child class.
        print(f'{self.GetName()} weighs {self.GetWeight()} kg and is {self.GetAge()} years old.')


class Tiger(Cat):
    ## child class constructor params must extend parent's
    def __init__(self, Name, Weight, Age, Stripes):
        ## polymorphism, so need to call parent constructor too
        super().__init__(Name, Weight, Age)
        self.__Stripes = Stripes

    def GetStripes(self) -> int:
        return self.__Stripes

    def SetStripes(self, NewStripes: int):
        self.__Stripes = NewStripes

    def Roar(self):
        for i in range(self.GetStripes()):
            self.Meow()


def Test():
    print("\ntesting oop inheritance\n")

    Felix = Cat("Felix", 10.1, 10)
    Felix.Meow()
    Tony = Tiger("Tony", 57.9, 23, 18)
    Tony.Roar()
