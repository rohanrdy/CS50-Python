from random import randint
from sys import exit

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        continue
    else:
        if n < 0 or n == 0:
            pass
        else:
            break

x = randint(1, n)

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if g > x:
            print("Too large!")
        elif g < x:
            print("Too small!")
        else:
            exit("Just right!")