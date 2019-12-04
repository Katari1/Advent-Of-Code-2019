def parse_input(location):
    data=[]
    data1=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for i in lines[0].split(","):
        data.append(i)
    for z in lines[1].split(","):
        data1.append(z)
    return data,data1

def processwires(input):
    location=[]
    pos=[]
    vert=0
    horiz=0


    for i in input:
        dir=i[0]
        dist=int(i[1:])
        pos=[0][0]
        for i in range(dist):
            if dir == 'U':
                vert += 1
            elif dir == 'D':
                vert -= 1
            elif dir == 'R':
                horiz += 1
            elif dir == 'L':
                horiz -= 1
            pos=(vert,horiz)
            location.append(pos)
    return location


#NOT NEEDED.  ABLE TO DO A SET INSTEAD
def intersectwire(input, input1):
    intersect=[]
    for i in input:
        for z in input1:
            if i == z:
                intersect.append(i)
    return intersect
#NOT NEEDED.  ABLE TO DO A SET INSTEAD

def smallest_distance(intersect):
    total = 0
    final = []
    for i in intersect:
        total = abs(i[0]) + abs(i[1])
        final.append(total)
    return final

def computesteps(intersections,wire1,wire2):
    steps=[]
    for i in intersections:
        index = wire1.index(i)
        index1 = wire2.index(i)
        steps.append(((index + 1)+(index1 + 1)))
    return steps

wire1=['R8','U5','L5','D3']
wire2=['U7','R6','D4','L4']

wire3,wire4 = parse_input('input.txt')


line1 = processwires(wire3)
line2 = processwires(wire4)
intersections = list(set(line1) & set(line2))
print min(computesteps(intersections,line1,line2))














