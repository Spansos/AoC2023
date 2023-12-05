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

def convert_number( n, convertinfo ):
    for ci in convertinfo:
        if n >= ci[1] and n < ci[1] + ci[2]:
            return n+ci[0]-ci[1]
    return n

def reverse_convert_number( n, i ):
    convertinfo = thing_to_things[i]
    for ci in convertinfo:
        if n >= ci[0] and n < ci[0] + ci[2]:
            return n+ci[1]-ci[0]
    return n

def smallest_dest( convertinfo, dissallowedsources ):
    sdest = -1
    for ci in convertinfo:
        for i in range(ci[2]):
            dest = ci[0]+i
            src = ci[1]+i
            if dest < sdest or sdest == -1:
                if not src in dissallowedsources:
                    sdest = dest
            else:
                break
    return sdest

def is_seed( n ):
    for i, j in zip(seeds[::2], seeds[1::2]):
        if n >= i and n < i+j:
            return True
    return False

sn = -1
n = 1
while not is_seed(n):
    sn += 1
    n = sn
    for i in range(len(thing_to_things)-1, -1, -1):
        n = reverse_convert_number( n, i )
    if not sn % 100000:
        print(sn)
print(sn)

# disallowed = [set() for i in range(len(thing_to_things))]
# while True:

#     # smallest pos anwser and from which converted
#     sdest, si = 100000000000000000, 0
#     for i, v in enumerate(thing_to_things):
#         dest = smallest_dest( v, disallowed[i] )
#         if dest <= sdest:
#             sdest = dest
#             si = i
#     print(sdest, si)
    
#     for i in range(si, -1, -1):
#         # fuck it, sdest and ssrc switched names
#         sdest, ssrc = reverse_convert_number( sdest, thing_to_things[i] ), sdest
#         disallowed[i].add(sdest)
#     # re-switched names
#     sdest, ssrc = ssrc, sdest
    
#     # print(ssrc)

#     print(disallowed)


#     # break

# # final_nums = []
# # for x, y in zip(seeds[::2], seeds[1::2]):
# #     for i in range(x, x+y):
# #         n = i
# #         for j in thing_to_things:
# #             n = convert_number( n, j )
# #         final_nums.append(n)
# # print(min(final_nums))