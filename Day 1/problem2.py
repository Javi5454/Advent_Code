import math

group = 4*[math.inf]
counter = 0

check_sum=0;
check = False

with open("./Inputs/input.txt","r") as archive:
    for line in archive.readlines():
        group = group[1:] + [int(line)]

        if check_sum % 6 == 0:
            check = True

        if(check):
            sum1 = sum(group[:3])
            sum2 = sum(group[1:])

            if sum1 < sum2:
                counter += 1
        else:
            check_sum +=1

print(counter)