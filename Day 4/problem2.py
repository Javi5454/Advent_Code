import math

list_matrix = []
whole_lines = []

with open("input.txt","r") as archive:
    order = archive.readline()

    for line in archive.readlines():
        if line != '\n':
            whole_lines.append(line)
print(len(whole_lines))
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

winner_number =0

for element in order:
    winner_number = int(element)
    if(len(list_matrix) != 1):
        for i in range(len(list_matrix)):
            for j in range(len(list_matrix[i])):
                for k in range(len(list_matrix[i][j])):
                    if list_matrix[i][j][k] == element:
                        list_matrix[i][j][k] = -1


        for matrix in list_matrix:
            for row in matrix:
                if sum(list(map(int, row))) == (-5):
                    ganador = list_matrix.index(matrix)
                    del list_matrix[ganador]

            if (matrix[0][0] == matrix[1][0] == matrix[2][0] == matrix[3][0] == matrix[4][0] == '-1'):
                ganador = list_matrix.index(matrix)
                del list_matrix[ganador]
            
            if (matrix[0][1] == matrix[1][1] == matrix[2][1] == matrix[3][1] == matrix[4][1] == '-1'):
                ganador = list_matrix.index(matrix)
                del list_matrix[ganador]
            if (matrix[0][2] == matrix[1][2] == matrix[2][2] == matrix[3][2] == matrix[4][2] == '-1'):
                ganador = list_matrix.index(matrix)
                del list_matrix[ganador]
            if (matrix[0][3] == matrix[1][3] == matrix[2][3] == matrix[3][3] == matrix[4][3] == '-1'):
                ganador = list_matrix.index(matrix)
                del list_matrix[ganador]
            if (matrix[0][4] == matrix[1][4] == matrix[2][4] == matrix[3][4] == matrix[4][4] == '-1'):
                ganador = list_matrix.index(matrix)
                del list_matrix[ganador]
    
        
                    
    else:
        for i in range(len(list_matrix)):
                for j in range(len(list_matrix[i])):
                    for k in range(len(list_matrix[i][j])):
                        if list_matrix[i][j][k] == element:
                            list_matrix[i][j][k] = -1
        break
sum = 0

for row in list_matrix[0]:
    for element in row:
        if int(element) != (-1):
            sum += int(element)

    
print(sum)
print(winner_number)
print(sum* winner_number)