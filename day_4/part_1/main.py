with open("part_1/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

sum = 0
for l in input:
    cinfo = l.split(':')[1]
    winning, have = cinfo.split('|')
    winning, have = winning.split(' '), have.split(' ')
    n = 0
    for i in have:
        if i in winning and i.isnumeric():
            n = n*2 if n else 1
    sum += n

print(sum)
