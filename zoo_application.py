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
    stat_current_locations = current_locations
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
    locations = [stat_current_locations, new_locations]

    for index, location in enumerate(locations):

        if index == 0:
            print()
            print("         Hayvanat Bahçesi Başlangıç Durumu           ")
            print()

        else:
            print()
            print("         Simülasyon Sonuçları            ")
            print()

        for animal_type, id_cap_loc in location.items():

            if "sheep" in animal_type:
                if "female" in animal_type:
                    number_of_female_sheep = len(id_cap_loc)
                    print("Dişi Koyun Sayısı: ", number_of_female_sheep)

                else:
                    number_of_male_sheep = len(id_cap_loc)
                    print("Erkek Koyun Sayısı: ", number_of_male_sheep)

            elif "cow" in animal_type:
                if "female" in animal_type:
                    number_of_female_cow = len(id_cap_loc)
                    print("Dişi İnek Sayısı: ", number_of_female_cow)

                else:
                    number_of_male_cow = len(id_cap_loc)
                    print("Erkek İnek Sayısı: ", number_of_male_cow)

            elif "chicken" in animal_type:
                number_of_chicken = len(id_cap_loc)
                print("Tavuk Sayısı: ", number_of_chicken)

            elif "cockerel" in animal_type:
                number_of_chicken = len(id_cap_loc)
                print("Tavuk Sayısı: ", number_of_chicken)

            elif "wolf" in animal_type:

                if "female" in animal_type:
                    number_of_female_wolf = len(id_cap_loc)
                    print("Dişi Kurt Sayısı: ", number_of_female_wolf)

                else:
                    number_of_male_wolf = len(id_cap_loc)
                    print("Erkek Kurt Sayısı: ", number_of_male_wolf)


            elif "lion" in animal_type:

                if "female" in animal_type:
                    number_of_female_lion = len(id_cap_loc)
                    print("Dişi Aslan Sayısı: ", number_of_female_lion)

                else:
                    number_of_male_lion = len(id_cap_loc)
                    print("Erkek Aslan Sayısı: ", number_of_male_lion)
            else:
                number_of_hunter = len(id_cap_loc)
                print("Avcı Sayısı:", number_of_hunter)



