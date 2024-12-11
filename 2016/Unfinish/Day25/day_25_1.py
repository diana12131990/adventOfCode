import re

f = open("day_25_input.txt","r")

def execute(program, a_value):
    registers = { 'a': a_value, 'b': 0, 'c': 0, 'd': 0 }
    clock = []
    
    pc = 0
    while pc < len(program):
        instr = program[pc]
        if instr.startswith('cpy'):
            _, src, dst = instr.split()
            if src in registers:
                registers[dst] = registers[src]
            else:
                registers[dst] = int(src)
            pc += 1
        if instr.startswith('inc'):
            reg = instr.split()[1]
            registers[reg] += 1
            pc += 1
        elif instr.startswith('dec'):
            reg = instr.split()[1]
            registers[reg] -= 1
            pc += 1
        elif instr.startswith('jnz'):
            _, X, Y = re.split(' |,', instr)
            if (X in registers and registers[X] != 0) or (X not in registers and int(X) != 0):
                pc += int(Y)
            else:
                pc += 1
        elif instr.startswith('out'):
            reg = instr.split()[1]
            clock.append(registers[reg])
            if len(clock) > 2 and clock[-1] != (clock[-2] ^ 1):
                return False
            pc += 1
            
    return True

bl = []
for line in f:
    line = line.strip()
    bl.append(line)
f.close()

n = 1
while True:
    if execute(bl, n):
        print(n)
        break
    n += 1