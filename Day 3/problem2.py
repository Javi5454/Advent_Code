import math

def convert_to_string(list):

    s = [str(i) for i in list]

    result = "".join(s)

    return (result)

def bit_Oxygen (list, pos):
    zeros = 0
    ones = 0

    for element in list:
        if element[pos] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros <= ones:
        return 1
    else:
        return 0

def bit_CO2 (list,pos):
    zeros = 0
    ones = 0

    for element in list:
        if element[pos] == '0':
            zeros += 1
        else:
            ones += 1

    if zeros <= ones:
        return 0
    else:
        return 1

def calculate_Oxygen (list,pos):

    if len(list) != 1:
        select = bit_Oxygen(list, pos)

        aux = []

        for element in list:
            if int(element[pos]) == select:
                aux.append(element)

        pos += 1

        list = calculate_Oxygen(aux,pos)

    return list


def calculate_CO2 (list,pos):

    if len(list) != 1:
            select = bit_CO2(list, pos)

            aux = []

            for element in list:
                if int(element[pos]) == select:
                    aux.append(element)

            pos += 1

            list = calculate_CO2(aux,pos)

    return list


init_list = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        aux = []
        for element in line:
            if element != '\n':
                aux.append(element)

        init_list.append(convert_to_string(aux))

pos = 0

oxygen = calculate_Oxygen(init_list,pos)
co2 = calculate_CO2(init_list,pos)

oxygen = convert_to_string(oxygen)
co2 = convert_to_string(co2)

oxygen = int(oxygen,2)
co2 = int(co2,2)

print("Oxygen generator rating:", oxygen)
print("CO2 scrubber rating:", co2)
print("Life support rating:", oxygen*co2)