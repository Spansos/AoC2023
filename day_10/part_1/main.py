import sys

sys.setrecursionlimit(100000)

with open("part_1/input.txt") as file:
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
handle = [ s ]
done = { s }
dists = {s: 0}

while handle:
    cur = handle.pop(0)
    for pos in loop[cur]:
        if pos in loop and pos not in done:
            done.add(pos)
            handle.append(pos)
            dists[pos] = dists[cur]+1

print(dists)
print(max(dists.values()))