import math

list_points = []
pair_points = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        pair_points = []

        line = line.strip()
        line = line.split(" -> ")

        point_to_add = []

        point = ""

        for i in range(len(line[0])):
            if line[0][i] == ',':
                last = i
                break
            else:
                point += line[0][i]

        point_to_add.append(int(point))

        point = ""

        for i in range(last+1,len(line[0])):
            point += line[0][i]
        point_to_add.append(int(point))

        pair_points.append(point_to_add)

        point = ""
        point_to_add = []

        for i in range(len(line[1])):
            if line[1][i] == ',':
                last = i
                break
            else:
                point += line[1][i]

        point_to_add.append(int(point))

        point = ""

        for i in range(last+1,len(line[1])):
            point += line[1][i]
        point_to_add.append(int(point))

        pair_points.append(point_to_add)

        list_points.append(pair_points)


matriz = [(1000*[0]) for x in range(1000)]

for element in list_points:
    if element[0][0] == element[1][0]:
        if element[0][1] <= element[1][1]:
            for i in range(element[0][1],element[1][1]+1):
                matriz[i][element[0][0]] += 1
        else:
            for i in range(element[1][1],element[0][1]+1):
                matriz[i][element[0][0]] += 1

    elif element[0][1] == element[1][1]:
        if element [0][0] <= element[1][0]:
            for i in range(element[0][0],element[1][0]+1):
                matriz[element[0][1]][i] += 1
        else:
            for i in range(element[1][0],element[0][0]+1):
                matriz[element[0][1]][i] += 1
    elif (abs(element[0][0]-element[1][0]) == abs(element[0][1]-element[1][1])):
        if element[0][0] < element[1][0]:
            if element[0][1] < element[1][1]:
                matriz[element[0][0]][element[0][1]] +=1
                while element[0][0] != element[1][0]:
                    element[0][0] += 1
                    element[0][1] +=1
                    matriz[element[0][0]][element[0][1]] +=1
            else:
                matriz[element[0][0]][element[0][1]] +=1
                while element[0][0] != element[1][0]:
                    element[0][0] += 1
                    element[0][1] -= 1
                    matriz[element[0][0]][element[0][1]] +=1
        else:
            if element[0][1] < element[1][1]: 
                matriz[element[1][0]][element[1][1]] += 1
                while element[0][0] != element[1][0]:
                    element[1][0] += 1
                    element[1][1] -= 1
                    matriz[element[1][0]][element[1][1]] +=1
            else:
                matriz[element[1][0]][element[1][1]] += 1
                while element[0][0] != element[1][0]:
                    element[1][0] += 1
                    element[1][1] += 1
                    matriz[element[1][0]][element[1][1]] +=1
                


result = 0

for row in matriz:
    for num in row:
        if num > 1:
            result +=1
print(matriz)
print(result)
