import re

def parse_keypad(input):
    keypad = {}
    for i, line in enumerate(input.splitlines()):
        for j, c in enumerate(line):
            keypad.update({c: (i,j)})
    return keypad

num_keypad = parse_keypad('''\
789
456
123
 0A
''')

dir_keypad = parse_keypad('''\
 ^A
<v>
''')

directions = {'>': (0,1), 'v': (1,0), '<': (0,-1), '^': (-1,0)}
cache = {}

def get_sequence_options(keypad, start, end):
    button_pos = set([pos for button, pos in keypad.items() if button != ' '])
    seq_options = []
    stack = [([], [], keypad[start])]
    while stack:
        seq, visited, pos = stack.pop()
        if pos == keypad[end]:
            seq_options.append(tuple(seq + ['A']))
            continue
        i, j = pos
        for move, d in directions.items():
            ni, nj = i + d[0], j + d[1]
            n_pos = (ni, nj)
            if n_pos in button_pos and n_pos not in visited:
                stack.append((seq + [move], visited + [n_pos], n_pos))
    return seq_options

def shortest_seq(seq, robot_offset, num_robots):
    if (seq, robot_offset, num_robots) in cache:
        return cache[(seq, robot_offset, num_robots)]

    if robot_offset == num_robots:
        result = len(seq)
    else:
        if robot_offset == 0:
            keypad = num_keypad
        else:
            keypad = dir_keypad

        prev_button = 'A'
        len_seq = 0

        for button in seq:
            options = []
            for next_seq in get_sequence_options(keypad, prev_button, button):
                options.append(shortest_seq(next_seq, robot_offset + 1, num_robots))

            len_seq += min(options)
            prev_button = button
        result = len_seq

    cache[(seq, robot_offset, num_robots)] = result
    return result

f = open("day_21_input.txt","r")

num_robots = 3
result = 0
for line in f:
    line = line.strip()
    len_seq = shortest_seq(line, 0, num_robots)
    result += len_seq * int(line[:-1])
f.close()

print(result)