from collections import Counter
f = open("input.txt", "r")
ll = []
rr = []
for line in f:
    left, right = line.split("   ")
    ll.append(int(left))
    rr.append(int(right))

ll.sort()
rr.sort()

sum1 = 0
for i in range(len(ll)):
    sum1 += abs(ll[i] - rr[i])

print(sum1)

counts = Counter(rr)

sum = 0
for x in ll:
    sum += x * counts[x]

print(sum)