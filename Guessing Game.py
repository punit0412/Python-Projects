import random as rnd


def guessgame(attempts):
    for chance in range(int(attempts)):
        num = input('Guess your number : ')
        auto_num = rnd.randint(0,10)
        if auto_num != num :
            print('Oops you guess a wrong number, try again !!!')
        else:
            print('\nCongratulations,You won')
    if chance == attempts-1:
        print('\nBetter Luck next time')


no_of_attempts = int(input('Enter number of attempts : '))
guessgame(no_of_attempts)