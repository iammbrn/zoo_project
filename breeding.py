from location import Location
from create_type import CreateType
from random import sample, choice, uniform
from math import sqrt

class Breeding():
    def __init__(self):
        self.create_type = CreateType()


    def calculate_distance(self, new_locations):

        gender = 0
        female = []
        male = []
        locations = []
        for animal_type, id_cap_locs in list(new_locations.items())[:-1]:
            for id_cap_loc in id_cap_locs:
                if gender%2 == 0:
                    female.append((animal_type, id_cap_loc))

                else:
                    male.append((animal_type, id_cap_loc))
                gender+=1
                locations.append(id_cap_loc[2])

        existing_locations = set(locations)
        fem_id = -1
        mal_id = -1
        for female_type, fem in female:
            id0, capacity, (x0, y0) = fem
            fem_id = max(fem_id, id0)

            for male_type, mal in male:
                id1, _, (x1, y1) = mal
                mal_id = max(mal_id, id1)

                distance = sqrt((x1 - x0)**2 + (y1 - y0)**2)

                if distance <= 3:
                    animal_type = choice([female_type, male_type])
                    while True:
                        new_loc_x = uniform(-250, 251)
                        new_loc_y = uniform(-250, 251)
                        if (new_loc_x, new_loc_y) not in existing_locations:
                            break

                    if animal_type == female_type:
                        new_id = sample(range(fem_id + 2, fem_id +3 ), 1)[0]
                        new_locations[animal_type].append([new_id, capacity, (new_loc_x, new_loc_y)])


                    else:
                        new_id = sample(range(mal_id + 2, mal_id + 3 ), 1)[0]
                        new_locations[animal_type].append([new_id, capacity, (new_loc_x, new_loc_y)])

        return new_locations

    def create_new_type(self):
        pass

if __name__ == "__main__":

    create_type = CreateType()
    all_types_dict = create_type.create_animals()

    location = Location()
    current_locations = location.random_current_location_generation(all_types_dict)

    breeding = Breeding()
    new_locations = breeding.calculate_distance(current_locations)

    for animal_type, id_cap_loc in new_locations.items():
        print(animal_type, id_cap_loc)
        print()
