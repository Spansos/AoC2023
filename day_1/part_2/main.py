with open("input.txt") as file:
    input = file.readlines()

sum = 0
letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for v in input:
    # print(v.strip())
    v = list(v)
    v1 = []
    for i, c in enumerate(v):
        for j, l in enumerate(letters):
            if len(v)-i >= len(l):
                # print(v[i:i+len(l)])
                if ''.join(v[i:i+len(l)]) == l:
                    v1.append(str(j+1))
        if v[i].isnumeric():
            v1.append(v[i])
    v = v1
    # print(v)
    v = int(v[0] + v[len(v)-1])
    sum += v

print(sum)