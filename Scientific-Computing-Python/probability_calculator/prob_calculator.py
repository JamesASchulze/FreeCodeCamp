import copy
import random

class Hat:
    def __init__(self,**args):
        self.ball_collection = []
        for color, qty in args.items():
            i = 0
            while i < qty:
                self.ball_collection.append(color)
                i += 1

        self.contents = copy.deepcopy(self.ball_collection)

        print(self.contents)

    def draw(self,num_to_remove):
        self.contents = copy.deepcopy(self.ball_collection)
        res = []
        
        if num_to_remove > len(self.contents):
            for ball in self.contents:
                res.append(ball)
        else:
            i = 0
        while i < num_to_remove:
            ball = self.contents.pop(random.randrange(0,len(self.contents)))
            res.append(ball)
          
            i += 1
        return res
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    matches = 0
    
    expected_ball_list = []
    for color, qty in expected_balls.items():
        i = 0
        while i < qty:
            expected_ball_list.append(color)
            i += 1
    
    i = 0
    while i < num_experiments:
        draw = hat.draw(num_balls_drawn)
        expected = copy.deepcopy(expected_ball_list)
        print("    draw {}: {}".format(i, draw))
        # print("expected: {}".format(expected))

        for d_ball in draw:
            for e_ball in expected:
                if (d_ball == e_ball):
                    expected.remove(e_ball)
                    # print("expected: {}".format(expected))
                    # print(e_ball)
            
            if (len(expected) == 0):
                matches += 1
                    
        # print("Matches: {}".format(matches))
        i += 1

    probability = matches / num_experiments
    return probability