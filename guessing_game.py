# program that'll get the details of each teams that join and print out how many teams have joined

class Teams:

    num_of_teams = 0

    def __init__(self, name, score = 0):
        
        self.name = name
        Teams.num_of_teams += 1
        self.score = score

    def save_team(self):
        team_details = 'Team Name: {}, with current score {}, Team number {}'.format(self.name, self.score, Teams.num_of_teams)
        return team_details
        
    def incr_score(self):
        self.score += 5
        return self.score
    
team_1 = Teams('Warriors')
#print(team_1.save_team())
# start the game:

import random

rand_num = random.randrange(0, 101)
count = 0
view = input('Do you want to view the high scores or play the game?(View/Play): ')

if view == 'View':
    myfile = open('highscore.txt' , 'r')
    sline = myfile.read()
    print(sline)
    myfile.close()
else:
    print('Guess a number between 0 and 100')
    print(rand_num)
        
    while count < 6:
        guess = int(input("Guess the number: "))
        if guess == rand_num:
            print("CONGRATS YOU GUESSED CORRECT!")
            team_1.incr_score()
            myfile = open('highscore.txt', 'a+')       
            myfile.write("\n" + team_1.name + "         " + str(team_1.score))
            stemp = myfile.read()
            print('Leaderboard is as follows:', "\n", stemp)
            myfile.close()
            break
        elif (rand_num - guess > 0) and (rand_num - guess < 10):
            print('YOU ARE CLOSE!')
            ask = input("Do you want a hint?(Yes/No): ")
            ask.lower()
            if ask == 'Yes':
                posnum = rand_num + 5
                negnum = rand_num - 5
                print('Hint: Number is somewhere between {0} and {1}'.format(negnum, posnum))
            count += 1
            print('You have {0} chances left!'.format(6-count))
                  
        elif (rand_num - guess < 0) and (rand_num - guess > -10):
            print('YOU ARE CLOSE!')
            ask = input("Do you want a hint?(Yes/No): ")
            ask.lower()
            if ask == 'Yes':
                posnum = rand_num + 5
                negnum = rand_num - 5
                print('Hint: Number is somewhere between {0} and {1}'.format(negnum, posnum))
            count += 1
            print('You have {0} chances left!'.format(6-count))
                  
        else:
            print('YOU GUESSED WRONG!')
            count += 2
            print('You have {0} chances left!'.format(6-count))
                  
        if count > 6:
            print('YOU LOST :((')
            break
