# advent of code 2021
# Puzzle 6
# What is the life support rating of the submarine?
from day_3_input import raw_input 

input = raw_input.splitlines()
oxygen_rating_list = list(input)
CO2_scrubber_list = list(input)

def get_freq_binary_number(list_binary_numbers, pos=True):
    # create a rate that has a counter in each digit position. positive if more 1's than 0's else negative
    rate = [0] * len(input[0])
    for number in list_binary_numbers:
        for i in range(len(number)):
            if int(number[i]):
                rate[i] += 1
            else:
                rate[i] -= 1

    if pos:
        return ['1' if x >= 0 else '0' for x in rate]
    return ['0' if x >= 0 else '1' for x in rate]

for i in range(len(input[0])):
    gamma_rate = get_freq_binary_number(oxygen_rating_list, True)
    oxy_numbers_to_remove = []
    for number in oxygen_rating_list:
        if number[i] != gamma_rate[i]:
            oxy_numbers_to_remove.append(number)
    oxygen_rating_list = [x for x in oxygen_rating_list if x not in oxy_numbers_to_remove]
    if len(oxygen_rating_list) == 1:
        oxygen_generator_rating = int(oxygen_rating_list[0], 2)

    epsilon_rate = get_freq_binary_number(CO2_scrubber_list, False) 
    CO2_numbers_to_remove = []
    for number in CO2_scrubber_list:
        if number[i] != epsilon_rate[i]:
            CO2_numbers_to_remove.append(number)
    CO2_scrubber_list = [x for x in CO2_scrubber_list if x not in CO2_numbers_to_remove]
    if len(CO2_scrubber_list) == 1:
        CO2_scrubber_rating = int(CO2_scrubber_list[0], 2)
        
life_support_rating = oxygen_generator_rating * CO2_scrubber_rating
print(life_support_rating)
