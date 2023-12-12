with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]
input = [[int(i) for i in j.split(' ') ] for j in input]

def diff( seq ):
    return [j-i for i, j in zip(seq, seq[1:])]

def do( seq ):
    if not any(seq):
        return seq
    v1 = seq[0]
    v2 = do( diff(seq) )[0]
    return [v1-v2] + seq

sum = 0
for i in input:
    sum += do(i)[0]
print(sum)