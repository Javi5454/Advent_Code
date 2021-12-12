from os import posix_fadvise


def find_conexiones(couples):
    conexions = {}
    routes = set()

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

    possible = [[True,'start',a] for a in conexions['start']]

    while (len(possible) != 0):
        last = possible.pop()

        next = [last + [a] for a in conexions[last[len(last)-1]]]

        for element in next:
            if element[len(element)-1] == "end":
                routes.add(tuple(element[1:]))
            elif element[len(element)-1] == "start":
                pass
            elif element[len(element)-1].isupper():
                possible.append(element)
            elif element.count(element[len(element)-1]) == 1:
                possible.append(element)
            elif element.count(element[len(element)-1]) == 2 and element[0] == True:
                possible.append([False]+element[1:])

    return routes

couples = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        line = line.strip().split('-')

        couples.append(line)

routes = find_conexiones(couples)

print(len(routes))