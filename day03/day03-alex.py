import string

with open("day03-alex.txt") as f:
    day03 = f.readlines()

day03 = [l.strip('\n\r') for l in day03]

def split_rucksack(rucksack):
    half = len(rucksack)//2
    return rucksack[:half], rucksack[half:]

rucksack = list(map(split_rucksack, day03))

def get_common(compartment):
    return list(set(compartment[0]) & set(compartment[1]))

commons = list(map(get_common, rucksack))

# get dict to assign values to letters
lower = dict(zip(list(string.ascii_lowercase), list(range(1, 27))))

upper = dict(zip(list(string.ascii_uppercase), list(range(27, 53))))

priorities = lower | upper # combine dicts

commons = sum(commons, []) # flatten list

sum([priorities.get(letter) for letter in commons]) # solution part 1



## part 2:

from utilspie import iterutils

part2 = list(iterutils.get_chunks(day03, 3))

def get_common_p2(elves):
    return list(set(elves[0]) & set(elves[1]) & set(elves[2]))

commons_p2 = sum(list(map(get_common_p2, part2)),[])

sum([priorities.get(letter) for letter in commons_p2]) # solution part 2
