import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**args):
        self.ball_collection = []
        for color, qty in args.items():
            # print("Color: {}, qty: {}".format(color, qty))
            i = 0
            while i < qty:
                self.ball_collection.append(color)
                i += 1

        self.contents = copy.deepcopy(self.ball_collection)

        print(self.contents)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass