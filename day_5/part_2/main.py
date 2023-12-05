with open("input.txt") as file:
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
    while left:
        lft = left.pop()
        for ci in convertinfo:
            ovrlp = overlap( lft, (ci[1],ci[1]+ci[2]) )
            if ovrlp[0] < ovrlp[1]:
                delta = ci[0]-ci[1]
                r.append( (ovrlp[0]+delta, ovrlp[1]+delta) )
                if ovrlp != lft:
                    lft1 = (lft[0], ovrlp[0])
                    lft2 = (ovrlp[1], lft[1])
                    if lft1[0] < lft1[1]: left.append(lft1)
                    if lft2[0] < lft2[1]: left.append(lft2)
                break
        else:
            r.append(lft)
    return r

def min_location( range_, thing_index ):
    if thing_index == len(thing_to_things):
        return range_[0]

    nxt_ranges = next_type( range_, thing_to_things[thing_index] )
    locations = [ min_location( i, thing_index+1 ) for i in nxt_ranges ]

    return min( locations )

seedranges = [(i, i+j) for i, j in zip(seeds[::2], seeds[1::2])]
locations = []
for seedrange in seedranges:
    locations.append( min_location(seedrange, 0) )
print(min(locations))