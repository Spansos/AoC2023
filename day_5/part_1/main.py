with open("part_1/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

seeds = [int(i) for i in input[0].replace('seeds: ', '').split(' ')]

thing_to_things = [ ]
n = -1
for i, v in enumerate(input[1:]):
    if v == '':
        thing_to_things.append([])
        n += 1
        continue
    if not v[0].isnumeric():
        continue
    thing_to_things[n].append(v)

thing_to_things = [ [(int(j.split(' ')[0]), int(j.split(' ')[1]), int(j.split(' ')[2])) for j in i] for i in thing_to_things ]

def convert_number( n, convertinfo ):
    for ci in convertinfo:
        if n >= ci[1] and n <= ci[1] + ci[2]:
            return n+ci[0]-ci[1]
    return n


final_nums = []
for i in seeds:
    n = i
    for j in thing_to_things:
        # print(n, j, end=' ')
        n = convert_number( n, j )
        # print(n, end='    ')
    final_nums.append(n)
print(min(final_nums))