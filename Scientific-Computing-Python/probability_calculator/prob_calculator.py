import copy
import random

class Hat:
    def __init__(self,**args):
        self.ball_collection = []
        for color, qty in args.items():
            for i in range(qty):
                self.ball_collection.append(color)
        
        self.contents = copy.deepcopy(self.ball_collection)

        print(self.contents)

    def draw(self,num_to_remove):
        self.contents = copy.deepcopy(self.ball_collection)
        res = []
        
        if num_to_remove > len(self.contents):
            for ball in self.contents:
                res.append(ball)
        else:
            for i in range(num_to_remove):
                ball = self.contents.pop(random.randrange(0,len(self.contents)))
                res.append(ball)
        return res
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    matches = 0
    
    expected_ball_list = []
    for color, qty in expected_balls.items():
        for i in range(qty):
            expected_ball_list.append(color)
    
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        try:
            for ball in expected_ball_list:
                draw.remove(ball)
        except:
            continue

        matches += 1
        
    probability = matches / num_experiments
    return probability