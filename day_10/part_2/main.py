import sys, math

sys.setrecursionlimit(100000)

with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

def get_neighbours( x, y ):
    r = []
    for d in ( (-1,0), (0,-1), (1,0), (0,1) ):
        pos = ( x+d[0], y+d[1] )
        if pos[0] >= 0 and pos[0] < len(input[0]) and pos[1] >= 0 and pos[1] < len(input):
            r.append(pos)
    return r

def get_connected( x, y ):
    connects = {(-1,0): {'-','L','F'}, (0,-1): {'|','7','F'}, (1,0): {'-','J','7'}, (0,1): {'|','L','J'}}
    r = []
    for n in get_neighbours( x, y ):
        c = input[n[1]][n[0]]
        dp = (n[0]-x,n[1]-y)
        dp2 = (x-n[0],y-n[1])
        if c in connects[dp] and (input[y][x] in connects[dp2] or input[y][x] == 'S' ):
            r.append(n)
    return tuple(r)

def get_loop( start, from_=None, end=None ):
    connected = get_connected(start[0],start[1])
    if not end:
        return { start:connected } | get_loop( connected[0], start, connected[1] )
    if start == end:
        return { start:connected }
    if connected[0] == from_:
        return { start:connected } | get_loop( connected[1], start, end )
    if len(connected) == 1 or connected[1] == from_:
        return { start:connected } | get_loop( connected[0], start, end )

def fill_thing( start, loop ):
    done = set()
    handle = [ start ]

    while handle:
        cur = handle.pop()
        done.add(cur)
        for d in ( (-1,0), (0,-1), (1,0), (0,1) ):
            pos = (d[0]+cur[0], d[1]+cur[1])
            if pos in done or pos[0] < 0 or pos[0] >= len(input[0]) or pos[1] < 0 or pos[1] >= len(input):
                continue
            if not pos in loop and not pos in done:
                handle.append(pos)
    
    return done

def is_inside( pos, loop ):
    done = set()
    handle = [ (pos[0]-.5, pos[1]-.5) ]

    h = []

    while handle:
        cur = handle.pop()
        h.append(cur)

        for d in ( (-1,0), (0,-1), (1,0), (0,1) ):
            pos = (d[0]+cur[0], d[1]+cur[1])

            if pos in done:
                continue

            if pos[0] < -.5 or pos[0] >= len(input[0])+.5 or pos[1] < -.5 or pos[1] >= len(input)+.5:
                return False

            if d == (-1,0):
                tpos1 = ( math.floor(cur[0]), math.ceil(cur[1]) )
                tpos2 = ( math.floor(cur[0]), math.floor(cur[1]) )
                if tpos1 not in loop.get(tpos2, ()) and tpos2 not in loop.get(tpos1, ()):
                    handle.append(pos)
            if d == (0,-1):
                tpos1 = ( math.ceil(cur[0]), math.floor(cur[1]) )
                tpos2 = ( math.floor(cur[0]), math.floor(cur[1]) )
                if tpos1 not in loop.get(tpos2, ()) and tpos2 not in loop.get(tpos1, ()):
                    handle.append(pos)
            if d == (1,0):
                tpos1 = ( math.ceil(cur[0]), math.ceil(cur[1]) )
                tpos2 = ( math.ceil(cur[0]), math.floor(cur[1]) )
                if tpos1 not in loop.get(tpos2, ()) and tpos2 not in loop.get(tpos1, ()):
                    handle.append(pos)
            if d == (0,1):
                tpos1 = ( math.ceil(cur[0]), math.ceil(cur[1]) )
                tpos2 = ( math.floor(cur[0]), math.ceil(cur[1]) )
                if tpos1 not in loop.get(tpos2, ()) and tpos2 not in loop.get(tpos1, ()):
                    handle.append(pos)

        done.add(cur)
    
    return True


found = False
for y, l in enumerate(input):
    for x, c in enumerate(l):
        if c == 'S':
            s = (x, y)
            found = True
            break
    if found:
        break

loop = get_loop(s)

tiles = set()
for y in range(len(input)):
    for x in range(len(input[0])):
        if (x,y) not in loop:
            tiles.add((x, y))

sections = []
while tiles:
    section = fill_thing( tiles.pop(), loop )
    tiles.difference_update( section )
    sections.append( section )

num = 0
while sections:
    section = sections.pop()
    if is_inside( section.pop(), loop ):
        num += len(section) + 1

print(num)

# r = is_inside( (10, 4), loop )
# r = [(math.floor(i[0]), math.floor(i[1])) for i in r]
# for y in range(len(input)):
#     for x in range(len(input[0])):
#         print('#' if (x,y) in r else '.', end='')
#     print()