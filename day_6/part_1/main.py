with open("part_1/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

times = [ int(i) for i in input[0].replace("Time:", "").strip().split(' ') if i ]
dists = [ int(i) for i in input[1].replace("Distance:", "").strip().split(' ') if i ]


s = 1
for time, dist in zip( times, dists ):
    n = 0
    for i in range(time+1):
        if i * (time-i) > dist:
            n += 1
    s *= n
print(s)