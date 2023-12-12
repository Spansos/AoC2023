with open("input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

rls = input[0]
input = [i.split('=') for i in input[2:]]
input = {i.strip():j.strip(' ()').split(',') for i,j in input}
input = {k:(v[0],v[1].strip()) for k,v in input.items() }

def next_k( curk, rli ):
    cur = input[curk]
    return cur[rls[rli%len(rls)]=='R']

patterns = {k:[] for k in input.keys() if k[2]=='Z'}
for k in patterns.keys():
    cur = k
    n = 0
    for i in range(0, 100000):
        cur = next_k( cur, n )
        n += 1
        if cur == k:
            if patterns[k]:
                patterns[k].append(n-sum(patterns[k]))
            else:
                patterns[k].append(n)



times = {k:() for k in input.keys() if k[2]=='A'}

for k in times.keys():
    cur = k
    n = 0
    while cur[2] != 'Z':
        cur = next_k( cur, n )
        n += 1
    times[k] = (n, patterns[cur][-1])

import math

print(times)
print(math.lcm(*[i[1] for i in times.values()]))