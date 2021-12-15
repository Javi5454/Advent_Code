def parse_input(input):
    conexions = {}

    with open(input,"r") as archive:
        chain = archive.readline().strip()

        for element in archive.readlines():
            if element != '\n':
                element = element.strip().split(" -> ")

                conexions[element[0]] = [element[1]]

    return chain, conexions


def convert_list(text):
    result = [str(text[i]) for i in range(len(text))]

    return result

chain, conexiones = parse_input("input.txt")

print("Template:", chain)

chain = convert_list(chain)

T = 40
for _ in range(T):
    new_chain = chain.copy()
    counter = 1

    for i in range(len(chain)-1):
        to_find = str(chain[i]) + str(chain[i+1])

        to_insert = str(conexiones[to_find][0])

        new_chain.insert(i+(1*counter), to_insert)
        counter += 1

    chain = new_chain.copy()

    print("After step", _+1)

chain = "".join(chain)

letters = []

for element in chain:
    if element not in letters:
        letters.append(element)

counter = len(letters)*[0]

for element in chain:
    counter[letters.index(element)] += 1

counter.sort()

result = counter[-1] - counter[0]

print(result)