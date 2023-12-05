with open("input.txt") as file:
    input = file.readlines()
input = [i.split(' ') for i in input]

sum = 0
for l in input:
    d = {}
    for n, c in zip(l[2::2], l[3::2]):
        c = c.rstrip(',;\n')
        d[c] = max(d.get(c, 0), int(n))
    if d.get('red', 0) <= 12 and d.get('green', 0) <= 13 and d.get('blue', 0) <= 14:
        sum += int(l[1][:-1])

print(sum)