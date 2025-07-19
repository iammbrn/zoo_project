from random import sample, choice
from math import sqrt
from create_type import CreateType
from location import Location
from breeding import Breeding
from hunting import Hunting


if __name__ == "__main__":

    create_type = CreateType()
    all_types_dict = create_type.create_animals()

    location = Location()
    current_locations = location.random_current_location_generation(all_types_dict)
    x = 0
    step_step_results = {}
    step = 1
    step_step_results = []
    for step in range(1000):
        breeding = Breeding()
        new_breedings = breeding.calculate_distance_for_breeding(current_locations)

        hunting = Hunting()
        new_huntings = hunting.calculate_distance_for_hunting(new_breedings)

        new_directions = location.random_direction_generation(new_huntings)
        new_locations = location.calculate_new_location(new_directions)
        current_locations = new_locations
        result =[]
        for animal_type, number_of_type in new_locations.items():

            result.append((animal_type, len(number_of_type)))
        step_step_results.append(result)


    """for result in step_step_results:
        print(result)
        print()"""


    for animal_type, id_cap_loc in new_locations.items():
        print(animal_type, len(id_cap_loc))








