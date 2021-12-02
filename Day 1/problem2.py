import math

group = 4*[math.inf]
counter = 0

check_sum=0;
check = False

with open("input.txt","r") as archive:
    for line in archive.readlines():
        group = group[1:] + [int(line)]

        sum1 = sum(group[:3])
        sum2 = sum(group[1:])

        if sum1 < sum2:
            counter += 1

print(counter)