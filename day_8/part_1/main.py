with open("input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

rls = input[0]
input = [i.split('=') for i in input[2:]]
input = {i.strip():tuple(j.strip(' ()').split(',')) for i,j in input}
input = {k:(v[0],v[1].strip()) for k,v in input.items()}

cur = 'AAA'
n = 0
while cur != 'ZZZ':
    rl = rls[n%len(rls)]
    n += 1
    cur = input[cur][rl == 'R']
print(n)