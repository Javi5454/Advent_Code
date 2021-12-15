from collections import Counter

def parse_input(input):
    conexions = {}

    with open(input,"r") as archive:
        chain = archive.readline().strip()

        for element in archive.readlines():
            if element != '\n':
                element = element.strip().split(" -> ")

                conexions[element[0]] = element[1]

    return chain, conexions



chain, conexiones = parse_input("input.txt")

print("Template:", chain)

counter = Counter()

for letter in chain:
    counter[letter] += 1

pairs = []

for i in range(len(chain)-1):
    to_add = "".join(chain[i:i+2])

    pairs.append(to_add)

pairs = Counter(pairs)

T = 40

for _ in range(T):
    current = Counter()

    for p, n in pairs.items():
        current[p[0]+conexiones[p]] += n
        current[conexiones[p]+p[1]] += n

        new_letter = conexiones[p]
        counter[new_letter] += n

    pairs = current

maximo = max(counter.values())
minimo = min(counter.values())

result = maximo - minimo

print(result)