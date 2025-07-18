from random import choice, sample
from math import sqrt
from create_type import CreateType


class Location():
    def __init__(self):
        self.directions = ["north", "west", "south", "east", "northwest", "northeast", "southwest", "southeast"]


    def random_current_location_generation(self, all_type_dict):
        all_location = {}
        total_ids = 0
        for id_capacity in all_type_dict.values():
            total_ids += len(id_capacity[0])

        x_coordinate = sample(range(-250, 251), total_ids)
        y_coordinate = sample(range(-250, 251), total_ids)
        x = 0
        y = 0

        for animal_type, id_capacity in all_type_dict.items():
            locations = []
            ids = id_capacity[0]
            capacity = id_capacity[1]


            for id in ids:
                locations.append([id, capacity, (x_coordinate[x], y_coordinate[y])])
                x += 1
                y += 1

            all_location[animal_type] = locations
        return all_location


    def random_direction_generation(self, current_locations):
        new_directions = {}
        for animal_type, id_cap_locs in current_locations.items():
            new_direction = []

            for id_loc in id_cap_locs:
                id = id_loc[0]
                capacity = id_loc[1]
                location = id_loc[2]
                x, y = location

                if x == 250 and y == 250:
                    directions = ["west", "south", "southwest"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif x == -250 and y == -250:
                    directions = ["north", "east", "northeast"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif x == 250 and y == -250:
                    directions =  ["north", "west", "northwest"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif x == -250 and y == 250:
                    directions =  ["north", "east", "northeast"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif x == 250:
                    directions =  ["north", "west", "south", "northwest", "southwest"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif x == -250:
                    directions =  ["north", "south", "east", "northeast", "southeast"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif y == 250:
                    directions =  ["west", "south", "east", "southwest", "southeast"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                elif y == -250:
                    directions =  ["north", "west", "east", "northwest", "northeast"]
                    direction = choice(directions)
                    new_direction.append([id, capacity, location, direction])

                else:
                    direction = choice(self.directions)
                    new_direction.append([id, capacity, location, direction])

            new_directions[animal_type] = new_direction

        return new_directions

    def calculate_new_location(self, new_directions):
        new_all_type_dic = {}
        for animal_type, id_cap_loc_dirs in new_directions.items():
            new_locations = []
            for id_cap_loc_dir in id_cap_loc_dirs:
                id = id_cap_loc_dir[0]
                move_capacity = id_cap_loc_dir[1]
                x, y = id_cap_loc_dir[2]
                direction = id_cap_loc_dir[3]

                if direction == "north":
                    x += move_capacity
                    new_location = (x, y)
                    new_locations.append([id, move_capacity, new_location])


                elif direction == "west":
                    y -= move_capacity
                    new_location = (x, y)
                    new_locations.append([id, move_capacity, new_location])

                elif direction == "south":
                    x -= move_capacity
                    new_location = (x, y)
                    new_locations.append([id, move_capacity, new_location])

                elif direction == "east":
                    y += move_capacity
                    new_location = (x, y)
                    new_locations.append([id, move_capacity, new_location])

                elif direction == "northwest":
                    capacity = sqrt((move_capacity ** 2) / 2)
                    x += capacity
                    y -= capacity
                    new_location = (round(x, 2), round(y, 2))
                    new_locations.append([id, move_capacity, new_location])

                elif direction == "northeast":
                    capacity = sqrt((move_capacity ** 2) / 2)
                    x += capacity
                    y += capacity
                    new_location = (round(x, 2), round(y, 2))
                    new_locations.append([id, move_capacity, new_location])

                elif direction == "southwest":
                    capacity = sqrt((move_capacity ** 2) / 2)
                    x -= capacity
                    y -= capacity
                    new_location = (round(x, 2), round(y, 2))
                    new_locations.append([id, move_capacity, new_location])

                elif direction == "southeast":
                    capacity = sqrt((move_capacity ** 2) / 2)
                    x -= capacity
                    y += capacity
                    new_location = (round(x, 2), round(y, 2))
                    new_locations.append([id, move_capacity, new_location])

                else:
                    pass
            new_all_type_dic[animal_type] = new_locations
        return new_all_type_dic






if __name__ == "__main__":

    """print("Random current location:",current_location)
    print("")

    print("Random direction:",direction)
    print("")

    print("New location:",new_location)"""

    create_types = CreateType()

    all_types_dict = create_types.create_animals()

    location = Location()

    """direction = location.random_direction_generation(directions)

    current_location = location.random_current_location_generation()

    new_location = location.calculate_new_location(current_location, direction, 4)"""

    current_locations = location.random_current_location_generation(all_types_dict)

    new_directions = location.random_direction_generation(current_locations)

    new_locations = location.calculate_new_location(new_directions)
    print("")
    print(new_locations["female_sheep_list"][0][0])
    print("")

    for old_location, new_location in zip(current_locations.items(), new_locations.items()):
        for old, new in zip(old_location, new_location):
            print(old)
            print(new)
            print("")
            print("")