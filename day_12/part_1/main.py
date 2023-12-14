with open("part_1/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]
arrangements, nums = [], []
for i in input:
    a, b = i.split(' ')
    arrangements.append(a)
    nums.append(b)
nums = [tuple([int(k) for k in j.split(',')]) for j in nums]

arrangements = [tuple([j for j in i.split('.')]) for i in arrangements]
brokens = []
starts = []
for i, ar in enumerate(arrangements):
    brokens.append([])
    starts.append([])
    for j, l in enumerate(ar):
        if l != '':
            brokens[-1].append(l)
            starts[-1].append(j+sum([len(k) for k in ar[:j]]))

import functools


@functools.cache
def get_arrangements( brokens, nums, starts ):
    if not nums and all([all([i!='#' for i in j]) for j in brokens]):
        print(brokens, nums, starts)
        return [[]]
    arrangements = []
    cur = nums[0]
    for i, arrangement in enumerate(brokens):
        curstart = starts[i]
        for j, c in enumerate(arrangement):
            if len(arrangement)-j >= cur:
                if j-1 >= 0 and brokens[i][j-1] == '#':
                    continue
                if j+cur < len(brokens[i]) and brokens[i][j+cur] == '#':
                    continue
                part1 = brokens[i][:max(j-1,0)]
                part2 = brokens[i][j+cur+1:]
                nbrokens = (*brokens[:i], ) + ((part1,) if part1 else ()) + ((part2,) if part2 else ()) + (*brokens[i+1:], )
                nstarts = []
                if part1: nstarts.append(curstart)
                if part2: nstarts.append(j+2+curstart)
                nstarts = tuple(nstarts+[v for p, v in enumerate(starts) if p != i])
                r = get_arrangements( nbrokens, nums[1:], nstarts )
                if r:
                    # print(brokens, nbrokens, repr(part1), repr(part2), cur,'|',curstart,starts, '|', i, j)
                    for s in r:
                        arrangements.append(list(range(j+curstart,j+cur+curstart)) + s)
                # print( 'nbr:', nbrokens, 'brkns:',brokens,'nm:', nums, 'nstrt:', nstarts, 'strt:',starts,'ar:', arrangements,'crstrt:', curstart,'cr:', cur,'i:',i,'j:', j,'r:',r )
                # else:
                #     arrangements.append(list(range(j+curstart,j+cur+curstart)))
    return arrangements
    
i = 5
fss = set([frozenset(i) for i in get_arrangements(tuple(brokens[i]), tuple(nums[i]), tuple(starts[i]))])
print(brokens[i], nums[i], starts[i], fss, len(fss))

# def num_pos( arrangement, nums ):