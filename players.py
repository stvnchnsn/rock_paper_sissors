import random

def test_main():
    steve = Random_Bot('Steve')
    d = steve.decision()
    steve.return_num_of_rounds_played()
    print(d)

def test_memory_bot_v1():
    pinky = Pinky("Pinky")
    d = pinky.decision()
    print(d)

protocol = test_memory_bot_v1

class Player:
    def __init__(self,name):
        self.playername = name
        self.points = 0
        self.num_of_rounds_played = 0
        self.selection = None
    def name(self):
        return self.playername
    def point(self,amount = 1):
        self.points += amount
    def score(self):
        return self.points
    def return_num_of_rounds_played(self):
        print(self.num_of_rounds_played)
        return self.num_of_rounds_played
    def decision(self):
        '''different for human or robot, so this method is overruled at the subclass level'''
        return self.selection
    def tell_results(self,result,opponent_choice):
        ''' Route the result to the robot'''
        pass
    
    
class Human(Player):
    def decision(self):
        self.selection = input("Rock(r), Paper(p) or Sissors(s)?: ")
        try:
            assert self.selection in ['r','p','s'],"invalid selection chooose 'r','p' or 's'"
        except AssertionError:
            error = True
            while error:
                self.selection = input("Rock(r), Paper(p) or Sissors(s)?: ")
                try:
                    assert self.selection in ['r','p','s']
                    error = False
                except AssertionError:
                    "invalid selection chooose 'r','p' or 's'"
        self.num_of_rounds_played +=1
        return self.selection

class Robot(Player):
    def __init__(self,name):
        super().__init__(name)
        self.hand_dict = {1:'r',2:'p',3:'s'}
        self.last_result = None
    def rand_1(self):
        self.selection = self.hand_dict[random.randint(1,3)]


class Random_Bot(Robot):
    '''returns random selection no matter what'''
    def decision(self):
        self.rand_1()
        self.num_of_rounds_played +=1
        return self.selection
class Pinky(Robot):
    def decision(self):
        self.num_of_rounds_played +=1
        if self.num_of_rounds_played == 1:
            self.rand_1()
            return self.selection
        else:
            if self.last_result == 0:
                '''play random'''
                self.rand_1()
                return self.selection
            if self.last_result == 1:
                '''play same'''
                return self.selection
            if self.last_result == -1:
                '''play oppoenets choice'''
                return self.last_opposing_choice
        
    def tell_results(self,result,opponent_choice):
        self.last_result = result
        self.last_opposing_choice = opponent_choice

if __name__ == '__main__':
    protocol()
