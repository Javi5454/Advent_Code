import math

counter = 0
last = math.inf

with open("input.txt","r") as archive:
    for line in archive.readlines():
        if last < int(line):
            counter +=1
        
        last = int(line)

print(counter)