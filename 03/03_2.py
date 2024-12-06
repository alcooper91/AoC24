import re

def mul_string(data):
    instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    val = 0
    for instruction in instructions:
        a, b = (instruction[4:len(instruction)-1]).split(',')
        val += int(a) * int(b)
    return val

data = open('input2.txt', 'r').read().replace('\n','')

data = "do()" + data

conds = re.split(r'don\'t\(\)', data)
val = 0
for cond in conds:
    match = re.search(r'do\(\)', cond)
    if match:
        val += mul_string(cond[match.end():])
    else:
        print(cond)
        print()
print(val)
