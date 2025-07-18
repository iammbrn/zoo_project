import random


class CreateType():

    def __init__(self):
        self.animals_dict = {
            "female_sheep_list": {"number": 15, "movement_capacity": 2},
            "male_sheep_list": {"number": 15, "movement_capacity": 2},
            "female_cow_list": {"number": 5, "movement_capacity": 2},
            "male_cow_list": {"number": 5, "movement_capacity": 2},
            "female_chicken_list": {"number": 10, "movement_capacity": 1},
            "male_cockerel_list": {"number": 10, "movement_capacity": 1},
            "female_wolf_list": {"number": 5, "movement_capacity": 3},
            "male_wolf_list": {"number": 5, "movement_capacity": 3},
            "female_lion_list": {"number": 4, "movement_capacity": 4},
            "male_lion_list": {"number": 4, "movement_capacity": 4}}
        self.all_types_dict = {}

    def create_animals(self, new_animals_dict = None):
        if new_animals_dict:
            for animal_type, number_capacity in new_animals_dict.items():

                number = number_capacity["number"]
                movement_capacity = number_capacity["movement_capacity"]

                if animal_type.startswith("female"):
                    animals_list = random.sample(range(0, (number * 2) + 1, 2), number)
                    self.all_types_dict[animal_type] = [animals_list, movement_capacity]
                else:
                    animals_list = random.sample(range(1, (number * 2) + 1, 2), number)
                    self.all_types_dict[animal_type] = [animals_list, movement_capacity]

            self.all_types_dict["hunter"] = [[1], 1]


        else:
            for animal_type, number_capacity in self.animals_dict.items():

                number = number_capacity["number"]
                movement_capacity = number_capacity["movement_capacity"]

                if animal_type.startswith("female"):
                    animals_list = random.sample(range(0, (number * 2) + 1, 2), number)
                    self.all_types_dict[animal_type] = [animals_list , movement_capacity]

                else:
                    animals_list = random.sample(range(1, (number * 2) + 1, 2), number)
                    self.all_types_dict[animal_type] = [animals_list , movement_capacity]

            self.all_types_dict["hunter"] = [[1], 1]

        return self.all_types_dict

    def create_new_animal(self):
        pass



if __name__ == "__main__":
    create_type = CreateType()
    all_types_dict = create_type.create_animals()
    for animal_type, id_capacity in all_types_dict.items():
        print(animal_type, id_capacity)
        print("")
