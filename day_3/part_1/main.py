with open("part_1/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

dirs = ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1))

sum = 0
for i, l in enumerate(input):
    n = 0
    count = False
    for j, c in enumerate(l):
        if c.isnumeric():
            n *= 10
            n += int(c)
            for dir in dirs:
                x = j+dir[0]
                y = i+dir[1]
                if x < 0 or x > len(l)-1 or y < 0 or y > len(input)-1:
                    continue
                if not input[y][x].isnumeric() and input[y][x] != '.':
                    count = True
        else:
            if count:
                sum += n
                count = False
            n = 0
    if count:
        sum += n
        count = False
    n = 0

print(sum)