## STACK

## According to Cambridge International

############################

SIZE = 5


def CreateStack():
	global Stack, TopPointer

	Stack = ["" for i in range(SIZE)]

	TopPointer = -1


############################

def Push(NewItem: str):
	global Stack, TopPointer

	if TopPointer == SIZE - 1:
		print("Stack is full")
	else:
		TopPointer += 1
		Stack[TopPointer] = NewItem
		print(Stack)


############################

def Pop():
	global Stack, TopPointer

	if TopPointer == -1:
		print("Stack is empty")
	else:
		Popped = Stack[TopPointer]
		Stack[TopPointer] = ""
		print(f"{Popped} was popped from the stack")

		TopPointer -= 1


############################

def Test():
	print("\ntesting stack\n")

	CreateStack()

	Pop()

	for Food in '''pizza
burger
salad
chocolate
noodles
pasta
curry
sushi'''.split("\n"):
		Push(Food)

	Pop()
	Pop()
	Pop()
	Push("eggs")
	Pop()

############################
