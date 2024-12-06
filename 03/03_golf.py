import re

data = open('input.txt', 'r').read().replace('\n','')
print(sum([int(match[1]) * int(match[2]) for match in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', data) ]))
print(sum([int(match[1]) * int(match[2]) for match in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', re.sub(r'don\'t\(\).*?(do\(\)|$)', '', data)) ]))

