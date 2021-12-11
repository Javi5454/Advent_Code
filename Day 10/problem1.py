from os import close
from typing import final

open_characters = ['(','[','{','<']
close_characters = [')',']','}','>']

completations = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        expected = '\n'
        line = line.strip()

        failed = False
        only_open = False
        
        while(only_open == False and failed == False):

            for i in range(len(line)):
                if line[i] in close_characters:

                    indx = close_characters.index(line[i])

                    expected = open_characters[indx]

                    if line[i-1] != expected:
                        failed = True
                        failed = True
                        break
                    else:
                        line = line[0:i-1:] + line[i+1: :]
                        break
                elif i == len(line)-1:
                    only_open = True

        if only_open:
            to_add = ""

            for i in range(len(line)-1, -1, -1):
                indx = open_characters.index(line[i])

                to_add += close_characters[indx]

            completations.append(to_add)

final_scores = []

for element in completations:
    result = 0

    for character in element:
        result *= 5

        if character == close_characters[0]:
            result += 1
        elif character == close_characters[1]:
            result += 2
        elif character == close_characters[2]:
            result += 3
        elif character == close_characters[3]:
            result += 4

    final_scores.append(result)

final_scores.sort()

final_indx = len(final_scores)/2

print(final_scores[final_indx-1])