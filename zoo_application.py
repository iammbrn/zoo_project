from random import sample, choice
from math import sqrt
from location import Location
from create_type import CreateType


class ZooApplication():
    def __init__(self, all_types_dict, directions):
        pass

    def moving(self,):
        pass



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


location = Location()

current_locations = location.random_current_location_generation(all_types_dict)

new_directions = location.random_direction_generation(current_locations)

new_locations = location.calculate_new_location(new_directions)

movement_capacity = {"sheep": 2, "cow": 2, "chicken": 1, "cockerel":1, "wolf": 3, "lion": 4, "hunter": 1}



wolf_hunting_distance = {"sheep": 4, "chicken": 4, "cockerel": 4}
lion_hunting_distance = {"sheep": 5, "cow": 5}
hunter_hunting_distance = {"sheep": 8, "cow": 8, "chicken": 8, "cockerel": 8, "wolf": 8, "lion": 8}


breeding_distance = 3


for step in range(1000):


    pass











