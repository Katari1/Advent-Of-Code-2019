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
    return result;


total = 0
for i in parse_input('input1.txt'):
    total += compute_fuel(i)

print total

