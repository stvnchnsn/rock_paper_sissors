import time
from players import Human
from players import Robot

def test_main():
    round = Round("Steve","Asmov")
    round.count_down()
    round.hand_analyzer()
protocol = test_main

class Round:
    def __init__(self,human,robot):
        self.human = Human(human)
        self.robot = Robot(robot)
    def count_down(self):
        for i in range(1,4):
            print(i)
            time.sleep(1)
        self.human_choice = self.human.choice()
        self.robot_choice = self.robot.choice()
    def hand_analyzer(self):
        hand_key = {'r':'Rock','p':'Paper','s':"Sissors"}
        print("{}'s choice: ".format(self.human.name()),hand_key[self.human_choice])
        print("{}'s choice: ".format(self.robot.name()),hand_key[self.robot_choice])
        winners = {'r':'s','p':'r','s':'p'}
        if self.human_choice == self.robot_choice:
            print('tie!')
        elif winners[self.human_choice] == self.robot_choice:
            self.human.point()
            print('{} Wins!'.format(self.human.name()))
        else:
            self.robot.point()
            print('{} Wins!'.format(self.robot.name()))
        

if __name__ =='__main__':
    protocol()