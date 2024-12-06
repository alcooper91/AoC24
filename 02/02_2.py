def is_ascending(a, b):
    return (a - b) > 0

def is_safe(data):
    ascending = is_ascending(data[0], data[1])
    for i in range(1, len(data)):
        a = data[i-1]
        b = data[i]
        if a == b:
            return False
        if ascending != is_ascending(a,b):
            return False
        diff = abs(a - b)
        if diff == 0 or diff > 3:
            return False
    
    return True

f = open('input.txt', 'r')

safe_count = 0
for l in f:
    data = [int(d) for d in l.split() ]
    if is_safe(data):
        safe_count += 1
    else:
        for i in range(len(data)):
            if is_safe(data[:i] + data[i+1:]):
                safe_count += 1
                break

print(safe_count)