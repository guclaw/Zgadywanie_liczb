from random import randint


def Zgadywanie_liczb():
    x = randint(1,100)
    # print(x)
    while True:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("It's not a number!")
            continue
        if guess == x:
            print('You win')
            break
        elif guess > x:
            print('to big!')
            continue
        else:
            print('to small!')
            continue

Zgadywanie_liczb()
