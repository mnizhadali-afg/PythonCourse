## ----------------- GuessNumberGame: -----------------------
## Prompts user to input a number to guess
## if the input is greater than the number, says: Too High,
## if the input is smaller than the number, says: Too Low,
## Program continues until the user finds the Correct Answer,
## If user finds the correct one, it says: Congratulations!

import random

number = random.randrange(1, 1000, 1)
n = 0
c = 0
numberOfTries = 0

while (n != number):
    n = int(input("Enter a number to guess OR (-1) to exit: "))
    if n == -1:
        print("See you next time. Bye!")
        exit()
    else:
        numberOfTries += 1

        if (numberOfTries >= 10):
            print("You Tried a lot. Better chance later.")
            exit()
        if n > number:
            print("Too High!")
        elif n < number:
            print("Too Low!")
        elif n == number:
            print("Congratulations! You Won.")
    c + 1
