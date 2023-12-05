with open("input.txt") as file:
    input = file.readlines()
input = [i.split(' ') for i in input]

sum = 0
for l in input:
    d = {}
    for n, c in zip(l[2::2], l[3::2]):
        c = c.rstrip(',;\n')
        d[c] = max(d.get(c, 0), int(n))
    sum += d['red']*d['green']*d['blue']

print(sum)