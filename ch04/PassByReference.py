inputInt = int(input("Enter the number of Loops: "))

def cubeIdLoop():
    for i in range(inputInt):
        print(i,"- ", 'id(number): ', id(i))
    print()
    print (f"Cube of {inputInt}:", inputInt ** 3)
cubeIdLoop()