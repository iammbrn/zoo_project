import random


class CreateAnimals():

    def __init__(self, number_animals):
        self.female_animal_list = []
        self.male_animal_list = []
        self.create_animals(number_animals)


    def create_animals(self, number_animals):
        animals_list = random.sample(range(1, number_animals + 1), number_animals)
        self.classification_animals(animals_list)

    def classification_animals(self, animals_list):


        for animal in animals_list:
            if animal % 2 == 0:
                self.female_animal_list.append(animal)

            else:
                self.male_animal_list.append(animal)

        return self.female_animal_list, self.male_animal_list


animals_dict = {
    "sheep": {"number": 30,"movement_capacity": 2},
    "cow": {"number": 10,"movement_capacity": 2},
    "chicken_cockerel": {"number": 20,"movement_capacity": 1},
    "wolf": {"number": 10,"movement_capacity": 3},
    "lion": {"number": 8,"movement_capacity": 4}}

all_types_dict = {}

for type, number_capacity in animals_dict.items():
    number = number_capacity["number"]
    movement_capacity = number_capacity["movement_capacity"]
    animals = CreateAnimals(number)
    if type != "chicken_cockerel":

        all_types_dict["female_" + type + "_list"]= [animals.female_animal_list, movement_capacity]
        all_types_dict["male_"+type+"_list"] = [animals.male_animal_list, movement_capacity]

    else:
        all_types_dict["chicken_list"] = [animals.female_animal_list, movement_capacity]
        all_types_dict["cockerel_list"]= [animals.male_animal_list,  movement_capacity]

all_types_dict["Hunter"] = [[1], 1]


if __name__ == "__main__":
    for type, id_capacity in all_types_dict.items():
        print(type, id_capacity)