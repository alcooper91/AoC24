import re

data = open('input.txt', 'r').read()

instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', data)

val = 0
for instruction in instructions:
    a, b = (instruction[4:len(instruction)-1]).split(',')
    val += int(a) * int(b)

print(val)