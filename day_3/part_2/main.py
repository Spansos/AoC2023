with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

dirs = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))

geardata = {}
for i, l in enumerate(input):
    n = 0
    count = False
    gears = set()
    for j, c in enumerate(l):
        if c.isnumeric():
            n *= 10
            n += int(c)
            for dir in dirs:
                x = j+dir[0]
                y = i+dir[1]
                if x < 0 or x > len(l)-1 or y < 0 or y > len(input)-1:
                    continue
                if not input[y][x].isnumeric() and input[y][x] == '*':
                    gears.add((x, y))
        else:
            for g in gears:
                geardata[g] = geardata.get(g, []) + [ n ]
            gears = set()
            n = 0
    for g in gears:
        geardata[g] = geardata.get(g, []) + [ n ]
    gears = set()
    n = 0


sum = 0
for i, v in geardata.items():
    if len(v) == 2:
        sum += v[0]*v[1]
print(sum)