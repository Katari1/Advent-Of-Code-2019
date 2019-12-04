def parse_input(puzzle_input):
    data=[]
    content = open(puzzle_input).readlines()
    for i in content:
        data.append(int(i.strip()))
    return data

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def compute_fuel(mass):
    result = truncate(mass/3)
    result=result - 2
    if result > 0:
        return result;
    else:
        return 0

def extend_fuel(mass):
    total = 0
    while mass > 0:
        mass = compute_fuel(mass)
        total += mass
        compute_fuel(mass)
    return total



sum = 0
for i in parse_input('input1.txt'):
    sum += extend_fuel(i)
print sum




