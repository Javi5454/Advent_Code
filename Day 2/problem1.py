import math

horizontal=0
depth = 0


import math

with open("input.txt","r") as data:
    for line in data.readlines():
        instructions = line.split()

        if instructions[0] == "forward":
            horizontal += int(instructions[1])
        elif instructions[0] == "down":
            depth += int(instructions[1])
        else:
            depth -= int(instructions[1])

print("Your position (horizontal,depth): (", horizontal, ",", depth, ")", sep="")
print("Result: ", horizontal*depth)