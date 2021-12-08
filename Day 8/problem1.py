from os import read, readlink


data = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        line = line.strip()
        line = line.split(' | ')

        data.append(line)

num_ones = 0
num_four = 0
num_seven = 0
num_eigth = 0

rep_one = ""
rep_four = ""
rep_seven = ""
rep_eight = ""

for element in data:
    """entry = element[0].split(' ')

    for combination in entry:
        if len(combination) == 2:
            rep_one = combination
        elif len(combination) == 4:
            rep_four = combination
        elif len(combination) == 3:
            rep_seven = combination
        elif len(combination) == 7:
            rep_eight = combination"""

    output = element[1].split(' ')

    for out in output:
        if len(out) == 2:
            num_ones += 1
        elif len(out) == 4:
            num_four += 1
        elif len(out) == 3:
               num_seven += 1
        elif len(out) == 7:
               num_eigth += 1

print(num_ones, num_four, num_seven, num_eigth)

result = num_ones + num_four + num_seven + num_eigth

print(result)