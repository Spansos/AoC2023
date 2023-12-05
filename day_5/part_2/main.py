with open("part_2/input.txt") as file:
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

def overlap( range1, range2 ):
    return ( max( range1[0], range2[0] ), min( range1[1], range2[1] ) )

def next_type( rng, convertinfo ):
    left = [ rng ]
    r = []
    for rng in left:
        for ci in convertinfo:
            
        
    for ci in convertinfo:
        ovrlp = overlap( rng, (ci[1],ci[1]+ci[2]) )
        delta = ci[0]-ci[1]
        r.append( ( ovrlp[0]+delta, ovrlp[1]+delta ) )
    if r:
        return r
    return rng

def min_location( range_, thing_index ):
    if thing_index == len(thing_to_things):
        return range_[0]

    locations = []
    for ci in thing_to_things[thing_index]:
        converted = convert( range_, ci )
        if converted[0] >= converted[1]:
            continue
        locations.append( min_location( converted, thing_index+1 ) )

    return min( locations )

seedranges = [(i, i+j) for i, j in zip(seeds[::2], seeds[1::2])]
locations = []
for seedrange in seedranges:
    locations.append( min_location(seedrange, 0) )
# print(locations)
print(convert( (79, 79+14), thing_to_things[0][0] ))

# print(convert((20, 30), (26, 22, 5)))