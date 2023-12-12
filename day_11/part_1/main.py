with open("part_1/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]
arrangements, nums = [], []
for i in input:
    a, b = i.split(' ')
    arrangements.append(a)
    nums.append(b)
nums = [[int(k) for k in j.split(',')] for j in nums]



brokens = []
for i in arrangements:
    brokens.append([])
    n = 0
    i = i.replace( '?', '.' )
    while True:
        n1 = i.find('#', n)
        if n1 == -1: break
        n2 = i.find('.', n1)
        if n2 == -1: n2 = len(i)
        brokens[-1].append((n1, n2-n1))
        n = n2
        if n == -1 or n == len(i): break

print(brokens)

# def num_pos( arrangement, nums ):