import random

def test_main():
    steve = Human('Steve')
    steve.choice()

protocol = test_main

class Player:
    def __init__(self,name):
        self.playername = name
        self.points = 0
    def name(self):
        return self.playername
    def point(self,amount = 1):
        self.points +=1
    def score(self):
        return self.points
class Human(Player):
    def choice(self):
        return input("Rock(r), Paper(p) or Sissors(s)?: ")

class Robot(Player):
    def choice(self):
        hand_dict = {1:'r',2:'p',3:'s'}
        return hand_dict[random.randint(1,3)]


if __name__ == '__main__':
    protocol()
