def create_set(data):
    result = set()

    for i in range(len(data)):
        result.add(data[i])

    return result

data = []

with open("input.txt","r") as archive:
    for line in archive.readlines():
        line = line.strip()
        line = line.split(' | ')

        data.append(line)

result = 0

for element in data:
    rep_one = ""
    rep_four = ""
    rep_seven = ""
    rep_eight = ""
    five_digits = []
    six_digits = []
    
    entry = element[0].split(' ')
    out = element[1].split(' ')

    for combination in entry:
        if len(combination) == 2:
            rep_one = combination
        elif len(combination) == 4:
            rep_four = combination
        elif len(combination) == 3:
            rep_seven = combination
        elif len(combination) == 7:
            rep_eight = combination
        elif len(combination) == 5:
            five_digits.append(combination)
        elif len(combination) == 6:
            six_digits.append(combination)


    orig_one = create_set(rep_one)
    orig_four = create_set(rep_four)
    orig_seven = create_set(rep_seven)
    orig_eight = create_set(rep_eight)

    for i in range(len(five_digits)):
        five_digits[i] = create_set(five_digits[i])

    for i in range(len(six_digits)):
        six_digits[i] = create_set(six_digits[i])

    up_segment, = orig_seven - orig_one

    posibble_nine = orig_four.copy()
    posibble_nine.add(up_segment)

    for i in range(len(six_digits)):
        if len(six_digits[i]-posibble_nine) == 1:
            final_nine = six_digits[i]
            six_digits.remove(six_digits[i])
            break

    for element in six_digits:
        if len(element-orig_one) == 4:
            final_zero = element
            six_digits.remove(element)
            break

    final_six = six_digits[0]

    for element in five_digits:
        if (len(final_six-element)) == 1:
            final_five = element
            five_digits.remove(element)
            break

    for element in five_digits:
        if(len(element - orig_seven)) == 2:
            final_three = element
            five_digits.remove(element)
            break

    final_two = five_digits[0]

    for i in range(len(out)):
        out[i] = create_set(out[i])

    final_numbers = [final_zero,orig_one,final_two,final_three,orig_four,
                     final_five,final_six,orig_seven,orig_eight,final_nine]
    
    val = 1000

    for i in range(len(out)):
        for j in range(len(final_numbers)):
            if out[i] == final_numbers[j]:
                result += j*val
        
        val /= 10

print(result)