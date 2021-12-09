matrix = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        line = line.strip()

        row_to_add = []

        for element in line:
            row_to_add.append(element)
        
        matrix.append(row_to_add)

result = 0

for i in range(len(matrix)):
    if i == 0:
        for j in range(len(matrix[i])):
            if j == 0:
                if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j+1]:
                    result += (int(matrix[i][j])+1)
            elif j == len(matrix[i])-1:
                if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]:
                    result += (int(matrix[i][j])+1)
            else:
                if matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                    result += (int(matrix[i][j])+1)

    elif i == len(matrix)-1:
        for j in range(len(matrix[i])):
            if j == 0:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j+1]:
                    result += (int(matrix[i][j])+1)
            elif j == len(matrix[i])-1:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1]:
                    result += (int(matrix[i][j])+1)
            else:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                    result += (int(matrix[i][j])+1)

    else:
        for j in range(len(matrix[i])):
            if j == 0:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j+1]:
                    result += (int(matrix[i][j])+1)
            elif j == len(matrix[i])-1:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1]:
                    result += (int(matrix[i][j])+1)
            else:
                if matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i+1][j] and matrix[i][j] < matrix[i][j-1] and matrix[i][j] < matrix[i][j+1]:
                    result += (int(matrix[i][j])+1) 

print(result)