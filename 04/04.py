
def build_string(lines, i, j, i_dir, j_dir, word):
    if i_dir == 0 and j_dir == 0:
        return None
    str_val = ""
    for x in range(len(word)):
        new_x = i+i_dir*x
        new_y = j+j_dir*x
        if new_x < 0 or new_x >= len(lines):
            return None
        if new_y < 0 or new_y >= len(lines[new_x]):
            return None
        # print(f'Len: {len(lines)}, Len Str: {len(lines[new_x])}, x={new_x}, y={new_y}')
        str_val += (lines[new_x][new_y])
    return str_val

def part1():
    lines = [ line.rstrip() for line in open('input.txt', 'r') ]
    val = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if (build_string(lines, i, j, x, y, 'XMAS') == 'XMAS'):
                        val += 1

    print(val)

# M . M
# . A .
# S . S

def check_mas(lines, i, j):
    if lines[i][j] != 'A':
        return False
    if i-1 < 0 or i+1 >= len(lines):
        return False
    if j-1 < 0 or j+1 >= len(lines[i]):
        return False
    vals = []
    for x, y in [(-1,-1), (-1, 1), (1,1), (1, -1)]:
        vals.append(lines[i+x][j+y])
    if vals.count('M') == 2 and vals.count('S') == 2 and vals[0] != vals[2]:
        print(vals)
        return True
    

def part2():
    lines = [ line.rstrip() for line in open('input.txt', 'r') ]
    val = 0
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if check_mas(lines, i, j):
                val += 1
    print(val)

part1()
part2()