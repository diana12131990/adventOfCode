import re

def process_gate(gate, values):
    in1, operator, in2, out = re.match(r'(\w+) (AND|OR|XOR) (\w+) -> (\w+)', gate).groups()
    if in1 in values and in2 in values:
        if operator == 'AND':
            values[out] = values[in1] & values[in2]
        elif operator == 'OR':
            values[out] = values[in1] | values[in2]
        elif operator == 'XOR':
            values[out] = values[in1] ^ values[in2]
        return True
    return False

def get_binary_num(values, prefix):
    return sum(values[f'{prefix}{i:02d}'] << i for i in range(len([z for z in values.keys() if z.startswith(prefix)])))

f = open("day_24_input.txt","r")

values = {}
gates = []
for line in f:
    line = line.strip()
    if "->" in line:
        gates.append(line)
    else:
        if line:
            x, val = line.split(': ')
            values[x] = int(val)
f.close()


while gates:
    for gate in gates:
        if process_gate(gate, values):
            gates.remove(gate)

x_num = get_binary_num(values, 'x') 
y_num = get_binary_num(values, 'y') 

correct_sum = bin(x_num + y_num)[2:]  # Binary representation of the sum
correct_z_values = {f'z{i:02d}': int(bit) for i, bit in enumerate(reversed(correct_sum))} 

swaps = sorted([z for z, val in correct_z_values.items() if z in values and values[z] != val])
print(', '.join(swaps))