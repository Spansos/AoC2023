with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]

times = [ i for i in input[0].replace("Time:", "").strip().split(' ') if i ]
dists = [ i for i in input[1].replace("Distance:", "").strip().split(' ') if i ]

time = int( ''.join(times) )
dist = int( ''.join(dists) )

def does_win( timepress, time, dist ):
    return timepress * (time-timepress) > dist

def calc( mintime, maxtime, time, dist ):
    half = (mintime + maxtime) // 2
    if mintime == half or maxtime == half:
        if does_win( maxtime, time, dist ):
            return maxtime
        else:
            return mintime
    if does_win( half, time, dist ):
        return calc( half, maxtime, time, dist )
    else:
        return calc( mintime, half, time, dist )

def calc2( mintime, maxtime, time, dist ):
    half = (mintime + maxtime) // 2
    if mintime == half or maxtime == half:
        if does_win( mintime, time, dist ):
            return mintime
        else:
            return maxtime
    if does_win( half, time, dist ):
        return calc2( mintime, half, time, dist )
    else:
        return calc2( half, maxtime, time, dist )


print(calc(0, time, time, dist) - calc2(0, time, time, dist) + 1)