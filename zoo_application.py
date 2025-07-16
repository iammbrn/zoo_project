import random
from math import sqrt

class ZooApplication():
    def __init__(self, all_types_dict, directions):
        pass

    def moving(self, type, current_location, directions, distance):
        direction = random.choice(directions)



    def breeding(self, type):
        pass

    def hunting(self, type):
        pass


northern_border = 250
western_border = -250
southtern_border = -250
eastern_border = 250


central_point = 0
movement_limit = sqrt(250 * 250 * 2)

directions = ["north", "west", "south", "east", "northwest", "northeast", "southwest", "southeast"]

"""sheep_movement_capacity = 2
cow_movement_capacity = 2
chicken_movement_capacity = 1
cockerel_movement_capacity = 1
wolf_movement_capacity = 3
lion_movement_capacity = 4
hunter_movement_capacity = 1"""

movement_capacity = {"sheep": 2, "cow": 2, "chicken": 1, "cockerel":1, "wolf": 3, "lion": 4, "hunter": 1}



wolf_hunting_distance = {"sheep": 4, "chicken": 4, "cockerel": 4}
lion_hunting_distance = {"sheep": 5, "cow": 5}
hunter_hunting_distance = {"sheep": 8, "cow": 8, "chicken": 8, "cockerel": 8, "wolf": 8, "lion": 8}


breeding_distance = 3


for step in range(1000):


    pass











