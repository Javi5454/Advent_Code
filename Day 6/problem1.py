with open("input.txt","r") as archive:
    data=[int(x) for x in archive.readline().split(',')]

reduced_vector = 9*[0]

reduced_vector = [data.count(x) for x in range(9)]

time = 256

for day in range(time):
    new_fish = reduced_vector[0]

    for i in range(len(reduced_vector)-1):
        reduced_vector[i] = reduced_vector[i+1]

    reduced_vector[6] += new_fish
    reduced_vector[8] = new_fish

print(sum(reduced_vector))