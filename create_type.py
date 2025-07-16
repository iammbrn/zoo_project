import random


class CreateType():

    def __init__(self):
        self.animals_dict = {
            "sheep": {"number": 30, "movement_capacity": 2},
            "cow": {"number": 10, "movement_capacity": 2},
            "chicken_cockerel": {"number": 20, "movement_capacity": 1},
            "wolf": {"number": 10, "movement_capacity": 3},
            "lion": {"number": 8, "movement_capacity": 4}}
        self.all_types_dict = {}

        self.create_animals()

    def create_animals(self):
        for type, number_capacity in self.animals_dict.items():
            self.female_animal_list = []
            self.male_animal_list = []
            self.type = type

            number = number_capacity["number"]
            self.movement_capacity = number_capacity["movement_capacity"]

            animals_list = random.sample(range(1, number + 1), number)

            self.all_types_dict = self.classification_animals(animals_list)

        self.all_types_dict["Hunter"] = [[1], 1]
        return self.all_types_dict

    def classification_animals(self, animals_list):
        for animal in animals_list:
            if animal % 2 == 0:
                self.female_animal_list.append(animal)

            else:
                self.male_animal_list.append(animal)

        return self.read_type()

    def read_type(self):
        if self.type != "chicken_cockerel":

            self.all_types_dict["female_" + self.type + "_list"] = [self.female_animal_list, self.movement_capacity]
            self.all_types_dict["male_" + self.type + "_list"] = [self.male_animal_list, self.movement_capacity]

        else:
            self.all_types_dict["chicken_list"] = [self.female_animal_list, self.movement_capacity]
            self.all_types_dict["cockerel_list"] = [self.male_animal_list, self.movement_capacity]

        return self.all_types_dict


if __name__ == "__main__":
    create_type = CreateType()
    all_types_dict = create_type
    for type, id_capacity in all_types_dict.items():
        print(type, id_capacity)
        print("")