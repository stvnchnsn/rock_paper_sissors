import time
from players import Human
from players import Random_Bot
from players import Pinky
from players import TheBrain

def battle_of_the_bots(robots):
    robot1 = robots[0]
    robot2 = robots[1]
    choices = []
    for i in range(10000):
        round = Round(robot1,robot2)
        #round.count_down()
        round.players_choice()
        round.hand_analyzer()
        choices.append(round.results())
    print("{}'s score: ".format(robot1.name()),robot1.score())
    print("{}'s score: ".format(robot2.name()),robot2.score())



def human_v_robot(robot):
    human_name = input("What is human's name?: ")
    human = Human(human_name)
    
    choices = []
    for i in range(5):
        round = Round(human,robot)
        round.count_down()
        round.players_choice()
        round.hand_analyzer()
        print(robot.return_num_of_rounds_played())
        choices.append(round.results())
    print("{}'s score: ".format(human.name()),human.score())
    print("{}'s score: ".format(robot.name()),robot.score())
    print(choices)

protocol = battle_of_the_bots
asimov = Random_Bot('Asimov')
pinky = Pinky('Pinky')
brain = TheBrain("The Brain")
robot = [brain,pinky]

class Round:
    def __init__(self,Player1,Player2):
        self.player1 = Player1
        self.player2 = Player2
    def count_down(self):
        for i in range(1,4):
            print(i)
            time.sleep(1)
    def players_choice(self):
        self.player1_choice= self.player1.decision()
        self.player2_choice = self.player2.decision()
    def results(self):
        return  {self.player1.name():self.player1_choice,
        self.player2.name():self.player2_choice}
    def hand_analyzer(self):
        hand_key = {'r':'Rock','p':'Paper','s':"Sissors"}
        print("{}'s choice: ".format(self.player1.name()),hand_key[self.player1_choice])
        print("{}'s choice: ".format(self.player2.name()),hand_key[self.player2_choice])
        winners = {'r':'s','p':'r','s':'p'}
        if self.player1_choice == self.player2_choice:
            play1_results = 0
            play2_results = 0
            print('tie!')
        elif winners[self.player1_choice] == self.player2_choice:
            self.player1.point()
            play1_results = 1
            play2_results = -1
            print('{} Wins!'.format(self.player1.name()))
        else:
            self.player2.point()
            play1_results = -1
            play2_results = 1
            print('{} Wins!'.format(self.player2.name()))
        self.player1.tell_results(play1_results,self.player2_choice)
        self.player2.tell_results(play2_results,self.player1_choice)
        
if __name__ =='__main__':
    protocol(robot)