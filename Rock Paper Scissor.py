import random


class RPCGame:
    def __init__(self,chances):
        self.chances = chances

    def rule(self):
        print("---There are some rules of the game---\n "
              "Rock V/S Paper --> Rock Wins\n Rock V/S Scissor --> Rock Wins\n Paper V/S Scissor --> Scissor Wins")
        print(" For Rock enter 1 \n For Scissor enter 2\n For paper enter 3 ")
        print(f"There will be {self.chances} rounds at a time")
        print('Best of Luck')

    def StartGame(self):
        choices = [1, 2, 3]
        computer_score = 0
        user_score = 0
        for _ in range(self.chances):
            computer_choice = random.choice(choices)
            user_choice = int(input('Please choose one from R:1 P:2 & S:3 : '))
            if user_choice not in choices:
                print('Please Enter a valid choice')
            [computer_score,user_score] = self.rulebook(computer_choice,user_choice,computer_score,user_score)
        print(f"Result\n"
              f"Computer --> {computer_score}"
              f"User --> {user_score}")
        if computer_score > user_score:
            print('Oops, Unfortunately you loose this game...')
        elif computer_score < user_score:
            print('Congratulations,You Beats the Computer...')
            print('Game Over')
            print('-------------------------------------')
        else:
            print('The Game ends in a Draw...')
            print('We have to play a Special Round Now...\n')

            computer_score = 0
            user_score = 0

            while computer_score == user_score:

                computer_choice = random.choice(choices)
                user_choice = int(input('Please choose one from R:1 P:2 & S:3 : '))
                if user_choice not in choices:
                    print('Please Enter a valid choice')
                [computer_score,user_score] = self.rulebook(computer_choice, user_choice, computer_score, user_score)

            print(f"Result\n"
                  f"Computer --> {computer_score}\n"
                  f"User --> {user_score}\n")

            if computer_score > user_score:
                print('--Computer Wins the Special Round--')
                print('--Better Luck Next Time')
            elif computer_score < user_score:
                print('Congratulations,You Beats the Computer in Special Round..')
                print('Game Over')
                print('-------------------------------------')

    def rulebook(self,computer,user,computer_score,user_score):
        if computer == 1 and user == 1:
            print('--This rounds Draw--')
        elif computer == 1 and user == 2:
            print('--Computer Wins this round--')
            computer_score += 1
        elif computer == 1 and user == 3:
            print('--Computer Wins this round--')
            computer_score += 1
        elif computer == 2 and user == 2:
            print('--This rounds Draw--')
        elif computer == 2 and user == 1:
            print('Congratulations,You win this round..')
            user_score += 1
        elif computer == 2 and user == 3:
            print('Congratulations,You win this round..')
            user_score += 1
        elif computer == 3 and user == 3:
            print('--This rounds Draw--')
        elif computer == 3 and user == 1:
            print('Congratulations,You win this round..')
            user_score += 1
        elif computer == 3 and user == 2:
            print('--Computer Wins this round--')
            computer_score += 1
        return [computer_score,user_score]

if __name__ == '__main__':
    game = RPCGame(int(input('No of round : ')))
    game.rule()
    game.StartGame()





