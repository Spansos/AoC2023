with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

empty_rows = [i for i, v in enumerate(input) if all([i=='.' for i in v])]
empty_columns = []
for x in range(len(input[0])):
    if all([input[i][x]=='.' for i in range(len(input))]):
        empty_columns.append(x)

galaxies = []
for y, l in enumerate(input):
    y = y + len([i for i in empty_rows if i < y]) * 999999
    for x, c in enumerate(l):
        if c == '#':
            x = x + len([i for i in empty_columns if i < x]) * 999999
            galaxies.append( (x, y) )

n = 0
for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i+1:]:
        n += abs(g1[0]-g2[0])+abs(g1[1]-g2[1])


print(n)