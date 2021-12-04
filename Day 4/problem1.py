import math

list_matrix = []
whole_lines = []

with open("input.txt","r") as archive:
    order = archive.readline()

    for line in archive.readlines():
        if line != '\n':
            whole_lines.append(line)

new_matrix = []

total_pos = 0

for i in range(int(len(whole_lines)/5)):

    new_matrix = []

    j= 0

    while j < 5:
            new_matrix.append(whole_lines[total_pos])
            j += 1
            total_pos += 1

    list_matrix.append(new_matrix)

for i in range(len(list_matrix)):
    for j in range(len(list_matrix[i])):
        list_matrix[i][j] = list_matrix[i][j].strip()
        list_matrix[i][j] = list_matrix[i][j].split()

order = order.strip()
order = order.split(',')

stop = False

for element in order:
    if(stop == False):
        for i in range(len(list_matrix)):
            for j in range(len(list_matrix[i])):
                for k in range(len(list_matrix[i][j])):
                    if list_matrix[i][j][k] == element:
                        list_matrix[i][j][k] = -1


        for matrix in list_matrix:
            for row in matrix:
                if sum(list(map(int, row))) == (-5):
                    ganador = list_matrix.index(matrix)
                    stop = True
                    winner_number = int(element)
                    break
        
        if(stop == False):
            cols = []

            for matrix in list_matrix:
                for i in range(len(matrix[0])):
                    cols.append([row[i] for row in matrix])
                
                if sum(list(map(int, row))) == (-5):
                    ganador = list_matrix.index(matrix)
                    stop = True
                    winner_number = int(element)
                    break
    else:
        break

sum = 0

for row in list_matrix[ganador]:
    for element in row:
        if int(element) != (-1):
            sum += int(element)

    

print(sum* winner_number)