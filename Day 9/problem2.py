from abc import abstractproperty
import math

matrix = []

def count_horizontal(i,j, width, heigh):
    result = 0

    if i == 0:
        for k in range(j+1, width):
            if int(matrix[i][k]) < 9 and int(matrix[i+1][k]) == 9:
                result +=1
            elif int(matrix[i][k]) == 9:
                break

        for k in range(j-1, -1, -1):
            if int(matrix[i][k]) < 9 and int(matrix[i+1][k]) == 9:
                result += 1
            elif int(matrix[i][k]) == 9:
                break
    
    elif i == heigh-1:
        for k in range(j+1, width):
            if int(matrix[i][k]) < 9 and int(matrix[i-1][k]) == 9:
                result +=1
            elif int(matrix[i][k]) == 9:
                break

        for k in range(j-1, -1, -1):
            if int(matrix[i][k]) < 9 and int(matrix[i-1][k]) == 9:
                result += 1
            elif int(matrix[i][k]) == 9:
                break

    else:
        for k in range(j+1, width):
            if int(matrix[i][k]) < 9 and int(matrix[i+1][k]) == 9 and int(matrix[i-1][k]) == 9:
                result +=1
            elif int(matrix[i][k]) == 9:
                break

        for k in range(j-1, -1, -1):
            if int(matrix[i][k]) < 9 and int(matrix[i+1][k]) == 9 and int(matrix[i-1][k]) == 9:
                result += 1
            elif int(matrix[i][k]) == 9:
                break

    return result

def count_basins(point, new_basin):
    horizontal_checked = []

    if point[0] == 0:
        if point[1] == 0:
            for j in range(len(matrix[point[0]])):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1,len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin +=1
                            
                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
        elif point[1] == len(matrix[point[0]])-1:
            for j in range(len(matrix[point[0]])-1, -1, -1):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1,len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break
        else:
            for j in range(point[1],len(matrix[point[0]])):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1,len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break
            for j in range(point[1]-1, -1, -1):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1,len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break

    elif point[0] == len(matrix)-1:
        if point[1] == 0:
            for j in range(len(matrix[point[0]])):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(len(matrix)-2, -1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break

        elif point[1] == len(matrix[point[0]]) - 1:
            for j in range(len(matrix[point[0]])-1, -1):
                if int(matrix[point[0]][j]) < 9:
                    new_basin +=1

                    for i in range(len(matrix)-2, -1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break
        else:
            for j in range(point[1],len(matrix[point[0]])):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]-1,-1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break
            for j in range(point[1]-1, -1, -1):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]-1,-1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break

    else:
        if point[1] == 0:
            for j in range(len(matrix[point[0]])):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1, len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break

                    for i in range(point[0]-1, -1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break

        elif point[1] == len(matrix[point[0]]) - 1:
            for j in range(len(matrix[point[0]])-1, -1, -1):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1, len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break

                    for i in range(point[0]-1, -1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break

        else:
            for j in range(point[1],len(matrix[point[0]])):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1, len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break

                    for i in range(point[0]-1, -1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break


            for j in range(point[1]-1, -1, -1):
                if int(matrix[point[0]][j]) < 9:
                    new_basin += 1

                    for i in range(point[0]+1, len(matrix)):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break

                    for i in range(point[0]-1, -1, -1):
                        if int(matrix[i][j]) < 9:
                            new_basin += 1

                            if i not in horizontal_checked:
                                new_basin += count_horizontal(i,j,len(matrix[0]),len(matrix))
                                horizontal_checked.append(i)
                        else:
                            break
                else:
                    break

    return new_basin


with open("input.txt","r") as archive:
    for line in archive.readlines():
        line = line.strip()

        row_to_add = []

        for element in line:
            row_to_add.append(element)
        
        matrix.append(row_to_add)

low_points = []

for i in range(len(matrix)):
    if i == 0:
        for j in range(len(matrix[i])):
            if j == 0:
                if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j+1]:
                    new_point = [i,j]
                    low_points.append(new_point)
            elif j == len(matrix[i])-1:
                if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]:
                    new_point = [i,j]
                    low_points.append(new_point)
            else:
                if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                    new_point = [i,j]
                    low_points.append(new_point)

    elif i == len(matrix)-1:
        for j in range(len(matrix[i])):
            if j == 0:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1]:
                    new_point = [i,j]
                    low_points.append(new_point)
            elif j == len(matrix[i])-1:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1]:
                    new_point = [i,j]
                    low_points.append(new_point)
            else:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                    new_point = [i,j]
                    low_points.append(new_point)

    else:
        for j in range(len(matrix[i])):
            if j == 0:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j+1]:
                    new_point = [i,j]
                    low_points.append(new_point)
            elif j == len(matrix[i])-1:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]:
                    new_point = [i,j]
                    low_points.append(new_point)
            else:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                    new_point = [i,j]
                    low_points.append(new_point) 


basins = []

for element in low_points:
    new_basin = 0

    new_basin = count_basins(element,new_basin)

    basins.append(new_basin)

maxs = []

last = basins[0]

print(basins)

while(len(maxs) != 3):
    for element in basins:
        if element > last:
            to_add = element
            last = element
    
    last = basins[0]
    basins.remove(to_add)
    maxs.append(to_add)
        

result = 1

for i in range(len(maxs)):
    result *= maxs[i]

print(result)