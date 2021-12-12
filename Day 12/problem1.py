def find_conexion(couples):
    conexions = {}

    for element in couples:
        a,b = element

        if a in conexions:
            conexions[a].append(b)
        else:
            conexions[a] = [b]

        if b in conexions:
            conexions[b].append(a)
        else:
            conexions[b] = [a]

    posibble = [["start",a] for a in conexions["start"]]
    routes = set()

    while len(posibble) != 0:
        last = posibble.pop()

        next = [last + [a] for a in conexions[last[len(last)-1]]]

        for element in next:
            if element[len(element)-1] == "end":
                routes.add(tuple(element))
            elif element[len(element)-1].isupper():
                posibble.append(element)
            elif element.count(element[len(element)-1]) == 1:
                posibble.append(element)

    return routes


couples = []

with open("input.txt","r") as  archive:
    for line in archive.readlines():
        line = line.strip().split('-')

        couples.append(line)

routes = find_conexion(couples)

print(len(routes))