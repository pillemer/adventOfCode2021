# advent of code 2021
# Puzzle 5
# What is the power consumption of the submarine?
from day_3_input import raw_input 

input = raw_input.splitlines()
rate = [0] * len(input[0])

# create a gamma rate that has a counter in each digit position. positive if more 1's than 0's else negative
for number in input:
    for i in range(len(number)):
        if int(number[i]):
            rate[i] += 1
        else:
            rate[i] -= 1

# translate negative/positive numbers to binary
epsilon_rate = ['0' if x > 0 else '1' for x in rate]
gamma_rate = ['1' if x > 0 else '0' for x in rate]

# translate binary number to decimal
gamma_rate = int(''.join(gamma_rate), 2)
epsilon_rate = int(''.join(epsilon_rate), 2)

power_consumption = gamma_rate * epsilon_rate
print(power_consumption)

'release.py in tpo-main'