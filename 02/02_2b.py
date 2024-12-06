def is_ascending(a, b):
    return (a - b) > 0

def is_safe(data):
    diffs = [ (b - a) for a, b in zip(data, data[1:])]
    if all(diff in [1,2,3] for diff in diffs) or all(diff in [-1,-2,-3] for diff in diffs):
        return True

    pos = 0
    neg = 0
    zeroes = 0
    too_large = 0
    for diff in diffs:
        # If any diff is a larger gap than 3 then removing it won't fix it.
        if abs(diff) > 3:
            too_large += 1
        if diff == 0:
            zeroes += 1
        elif diff < 0:
            neg += 1
        else:
            pos += 1
    # More than one zero is an error
    if zeroes > 1:
        return False
    # If all three types have values, then there's at least two errors
    if zeroes > 0 and pos > 0 and neg > 0:
        return False
    # If we have more than one of each type, we have an error
    if pos > 1 and neg > 1:
        return False
    if too_large > 1:
        return False
    if pos > 0 and too_large > 0 and neg == 0:
        return False
    if neg > 0 and too_large > 0 and pos == 0:
        return False
    
    for i in range(len(diffs)):
        if abs(diffs[i]) > 3 :
            if (i + 1) >= len(diffs):
                return False
            if abs(diffs[i]+ diffs[i+1]) > 3:
                return False
    print (diffs)
    return True
    
    # There's one last potential recovery mode here which is that if we have exactly one positive/negative psir then there's a chance that by removing the too large value things are fine.

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