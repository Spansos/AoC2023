with open("input.txt") as file:
    input = file.readlines()

sum = 0
for v in input:
    v = [i for i in v if i.isnumeric()]
    v = int(v[0] + v[len(v)-1])
    # print(v)
    sum += v

print(sum)