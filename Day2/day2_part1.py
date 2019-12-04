def parse_input(puzzle_input):
    data=[]
    content = open(puzzle_input).read()
    lines = content.split(',')
    for l in lines:
        if l.strip():
            data.append(int(l))
    return data


def compute_intcode(input):
    pos = 0
    optcode = input[pos + 0]
    while optcode > 0 and optcode < 3:
        optcode = input[pos + 0]
        if optcode == 1:
            pos1 = input[input[pos + 1]]
            pos2 = input[input[pos + 2]]
            total = pos1 + pos2
            input[input[pos + 3]] = total

        if  optcode == 2:
            pos1 = input[input[pos + 1]]
            pos2 = input[input[pos + 2]]
            total = pos1 * pos2
            input[input[pos + 3]] = total
        pos += 4
    return input




data = parse_input('input.txt')
data[1] = 12
data[2] = 2
print compute_intcode(data)


