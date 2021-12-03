import math

def convert(list):

    # Converting integer list to string list
    s = [str(i) for i in  list]

    # Join the new list
    result = "".join(s)

    return (result)

zeros = 12*[0]
ones = 12*[0]

gamma_list = []
epsilon_list = []


with open("input.txt","r") as archive:
    for line in archive.readlines():
        
        position = 0

        for element in line:
            if element != '\n':
                if int(element) == 0:
                    zeros[position] += 1
                else:
                    ones[position] += 1  
            position +=1  

counter = 0

for element in zeros:
    if element > ones[counter]:
        gamma_list.append(0)
        epsilon_list.append(1)
    else:
        gamma_list.append(1)
        epsilon_list.append(0)
    
    counter += 1

gamma = convert(gamma_list)
epsilon = convert(epsilon_list)

gamma = int(gamma,2)
epsilon = int(epsilon,2)

print("Gamma number:",gamma)
print("Epsilon number:",epsilon)
print("Power consumption:", gamma*epsilon)