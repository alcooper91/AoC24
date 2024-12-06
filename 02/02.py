def is_ascending(a, b):
    return (a - b) > 0

f = open('input.txt', 'r')

safe_count = 0
for l in f:
    data = [int(d) for d in l.split() ]
    ascending = is_ascending(data[0], data[1])
    is_safe = True
    for i in range(1, len(data)):
        a = data[i-1]
        b = data[i]
        if a == b:
            is_safe = False
            break
        if ascending != is_ascending(a,b):
            is_safe = False
            break
        diff = abs(a - b)
        if diff == 0 or diff > 3:
            is_safe = False
            break
    if is_safe:
        safe_count += 1

print(safe_count)