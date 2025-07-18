from create_type import CreateType
from location import Location
from math import sqrt


class Hunting():

    def __init__(self):
        self.wolf_hunting_distance = 4
        self.lion_hunting_distance = 5
        self.hunter_hunting_distance = 8

    def calculate_distance_for_hunting(self, new_locations):

        wolf_locations = []
        wolf_huntings = []
        lion_locations = []
        lion_huntings = []
        hunter_location = []
        hunter_hunting = []
        x = 0
        for animal_type, id_cap_locs in new_locations.items():

            for id_cap_loc in id_cap_locs:

                if "wolf" in animal_type:
                    wolf_locations.append((animal_type, id_cap_loc[0], id_cap_loc[2], self.wolf_hunting_distance))
                elif ("chicken" in animal_type) or ("cockerel" in animal_type):
                    wolf_huntings.append((animal_type, id_cap_loc[0], id_cap_loc[2]))
                elif ("sheep" in animal_type):
                    wolf_huntings.append((animal_type, id_cap_loc[0], id_cap_loc[2]))
                    lion_huntings.append((animal_type, id_cap_loc[0], id_cap_loc[2]))
                elif "lion" in animal_type:
                    lion_locations.append((animal_type, id_cap_loc[0], id_cap_loc[2], self.lion_hunting_distance))
                elif ("cow" in animal_type):
                    lion_huntings.append((animal_type, id_cap_loc[0], id_cap_loc[2]))

                elif "hunter" in animal_type:
                    hunter_location.append((animal_type, id_cap_loc[0], id_cap_loc[2], self.hunter_hunting_distance))
                if "hunter" not in animal_type:
                    hunter_hunting.append((animal_type, id_cap_loc[0], id_cap_loc[2]))

        hunting_list = [(wolf_locations, wolf_huntings), (lion_locations, lion_huntings), (hunter_location, hunter_hunting)]

        for hunters, huntings in hunting_list:

            for hunter in hunters:
                animal_type0, _, (x0, y0), hunting_distance = hunter

                for hunting in huntings:
                    animal_type1, id, (x1, y1) = hunting

                    distance = sqrt(((x1 - x0)**2) + ((y1- y0)**2))

                    if distance <= hunting_distance:
                        new_locations = self.delete_animal(new_locations, animal_type1, id)

        return new_locations

    def delete_animal(self, new_locations, animal_type, id):
        for animal_types, id_cap_locs in new_locations.items():
            for index, id_cap_loc in enumerate(id_cap_locs):
                if animal_types == animal_type and id_cap_loc[0] == id:
                    new_locations[animal_type].pop(index)

        return new_locations



if __name__ == "__main__":
    create_type = CreateType()
    all_type_dict = create_type.create_animals()
    location = Location()
    current_locations = location.random_current_location_generation(all_type_dict)

    hunting = Hunting()
    hunting.calculate_distance_for_hunting(current_locations)
