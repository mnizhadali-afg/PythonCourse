import random

def add(x, y):
    return x + y

print('--------- Have fun with Randomize Addition Game ---------')

for i in range(0, 5, 1):
    print("Randomizing First Number ... OK. Done! ")
    num1 = random.randrange(1, 10, 1)
    print("Number is: ", num1, '\n')

    print("Randomizing Second Number ... OK. Done! ")
    num2 = random.randrange(1, 10, 1)
    print("Number is: ", num2, '\n')

    # n1 = int(input("Enter the first Number: "))
    # n2 = int(input("Enter the second Number: "))
    if (num1 == -1 or num2 == -1):
        print('Not valid input. Bye!')
        # break
        exit()
    else:
        print('[Result: ', add(num1, num2), ']\n')