def parse_input(input):

    with open(input,"r") as archive:
        dots = []

        for line in archive.readlines():
            if line[0] == 'f':
                instruction = line.strip()
                break
            else:
                if line != '\n':
                    line = line.strip().split(',')

                    dots.append(line)

    return dots, instruction

dots, instruction = parse_input("input.txt")     


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

instruction = instruction.split("fold along ")
instruction = instruction[1]

instruction = instruction.split("=")


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

for i in range(len(bool_matrix)):
    for j in range(len(bool_matrix[i])):
        if bool_matrix[i][j] == True:
            result += 1

print(result)