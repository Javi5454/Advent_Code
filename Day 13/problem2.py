def parse_input(input):

    with open(input,"r") as archive:
        dots = []
        instructions = []

        for line in archive.readlines():
            if line[0] == 'f':
                instruction = line.strip().split("fold along ")
                instructions.append(instruction[1].split('='))
            else:
                if line != '\n':
                    line = line.strip().split(',')

                    dots.append(line)

    return dots, instructions

dots, instructions = parse_input("input.txt")     


for i in range(len(dots)):
    for j in range(len(dots[i])):
        dots[i][j] = int(dots[i][j])

max_x = 0
max_y = 0

for element in dots:
    if element[0] > max_x:
        max_x = element[0]

    if element[1] > max_y:
        max_y = element[1]

bool_matrix = [((max_x+1)*[False]) for x in range(max_y+1)]

for element in dots:
    bool_matrix[element[1]][element[0]] = True


for instruction in instructions:
    
    if instruction[0] == 'y':
        for j in range(int(instruction[1])+1, len(bool_matrix)):
            for i in range(len(bool_matrix[j])):
                if bool_matrix[j][i] == True:
                    distance = j - int(instruction[1])
                    bool_matrix[int(instruction[1])-distance][i] = True
                    bool_matrix[j][i] = False


    elif instruction[0] == 'x':
        for i in range(int(instruction[1])+1, len(bool_matrix[int(instruction[1])])):
            for j in range(len(bool_matrix)):
                if bool_matrix[j][i] == True:
                    distance = i - int(instruction[1])
                    bool_matrix[j][int(instruction[1])-distance] = True
                    bool_matrix[j][i] = False

result = 0

final_dots = []

for i in range(len(bool_matrix)):
    for j in range(len(bool_matrix[i])):
        if bool_matrix[i][j] == True:
            final_dots.append([j,i])

max_x = 0
max_y = 0

for element in final_dots:
    if element[0] > max_x:
        max_x = element[0]

    if element[1] > max_y:
        max_y = element[1]

grid = [[' '] *(max_x+1) for _ in range(max_y+1)]

for x, y in final_dots:
    grid[y][x] = "@"

for r in grid:
    print("".join(r))