# advent of code 2021
# Puzzle 4
# What do you get if you multiply your final horizontal position by your final depth?
from puzzle_3_input import raw_input 

input = raw_input.splitlines()

horizontal_position = 0
aim = 0
depth = 0

for entry in input:
    amount = [int(x) for x in entry.split() if x.isdigit()][0]
    if entry.startswith('f'):
        horizontal_position += amount
        depth += amount * aim
    elif entry.startswith('u'):
        aim -= amount
    else: 
        aim += amount

print(f'horizontal_position: {horizontal_position}')
print(f'depth: {depth}')
print(f'final result = {depth * horizontal_position}')
