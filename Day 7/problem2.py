import math

with open("input.txt","r") as archive:
    data=[int(x) for x in archive.readline().split(',')]

max = 0
for element in data:
    if element > max:
        max = element

result = math.inf
for i in range(max+1):
    sum = 0
    for element in data:
        acumulate = abs(element-i)
        acumulate = (acumulate*(acumulate+1))/2
        sum += acumulate

    if sum < result:
        result = sum


print(result)