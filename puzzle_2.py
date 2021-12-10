# advent of code 2021
# Puzzle 2
# count the number of times the sum of measurements in this sliding window increases from the previous sum.
from day_1_input import raw_input 
from puzzle_1 import counter

input = [int(entry) for entry in raw_input.split()]

windows = []
for i in range(2, len(input)):
    windows.append(input[i] + input[i-1] + input[i-2])

counter(windows)
