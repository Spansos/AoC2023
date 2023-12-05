with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]


import functools 

@functools.cache
def scratchcard( cardn ):
    cinfo = input[cardn-1].split(':')[1]
    winning, have = cinfo.split('|')
    winning, have = winning.split(' '), have.split(' ')
    n = 0
    for i in have:
        if i in winning and i.isnumeric():
            n += 1
    
    scratch_worth = 1
    for i in range( cardn+1, cardn+n+1 ):
        scratch_worth += scratchcard(i)
    return scratch_worth


total_scratch = 0
for i, v in enumerate(input):
    total_scratch += scratchcard( i+1 )
print(total_scratch)