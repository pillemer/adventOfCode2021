# advent of code 2021
# Puzzle 1
# How many measurements are larger than the previous measurement?
from day_1_input import raw_input 

input = [int(entry) for entry in raw_input.split()]

def counter(list_of_depths):
    deeper_count = 0
    shallower_count = 0
    prev_depth = list_of_depths[0]
    for depth in list_of_depths:
        if depth > prev_depth:
            deeper_count += 1
        elif depth < prev_depth:
            shallower_count += 1
        prev_depth = depth
        
    print(f'Deeper: {deeper_count}')
    print(f'Shallower: {shallower_count}')
