from random import sample, choice
from math import sqrt
from create_type import CreateType
from location import Location
from breeding import Breeding




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



movement_capacity = {"sheep": 2, "cow": 2, "chicken": 1, "cockerel":1, "wolf": 3, "lion": 4, "hunter": 1}



wolf_hunting_distance = {"sheep": 4, "chicken": 4, "cockerel": 4}
lion_hunting_distance = {"sheep": 5, "cow": 5}
hunter_hunting_distance = {"sheep": 8, "cow": 8, "chicken": 8, "cockerel": 8, "wolf": 8, "lion": 8}


breeding_distance = 3

if __name__ == "__main__":

    create_type = CreateType()
    all_types_dict = create_type.create_animals()

    location = Location()
    current_locations = location.random_current_location_generation(all_types_dict)
    x = 0
    for step in range(1000):
        breeding = Breeding()
        new_breedings = breeding.calculate_distance(current_locations)

        new_directions = location.random_direction_generation(new_breedings)
        new_locations = location.calculate_new_location(new_directions)
        current_locations = new_locations
        print(x)
        x += 1

    for type, id_cap_loc in new_locations.items():
        print(type, len(id_cap_loc))

    print()












