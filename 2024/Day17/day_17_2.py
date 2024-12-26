
A = 30899381
B = 0
C = 0
program = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]
output = []

def decode(combo_operand):
    if combo_operand < 4:
        return combo_operand 
    elif combo_operand == 4:
        return A
    elif combo_operand == 5:
        return B
    elif combo_operand == 6:
        return C

program_string = ",".join(map(str, program))
candidates = [""]
for counter in range(len(program)):
    new_candidates = []
    for a_octal in candidates:
        for x in range(8):
            new_a_octal = a_octal + str(x)
            A  = int(new_a_octal, 8)
            instruction_pointer = 0
            output = []
        
            while instruction_pointer < len(program):
                opcode = program[instruction_pointer]
                operand = program[instruction_pointer + 1]
        
                if opcode == 0:  # adv
                    A = int(A / (2 ** decode(operand)))
                elif opcode == 1:  # bxl
                    B ^= operand
                elif opcode == 2:  # bst
                    B = decode(operand) % 8
                elif opcode == 3:  # jnz
                    if A != 0:
                        instruction_pointer = operand
                        continue
                elif opcode == 4:  # bxc
                    B ^= C
                elif opcode == 5:  # out
                    output.append(decode(operand) % 8)
                elif opcode == 6:  # bdv
                    B = int(A / (2 ** decode(operand)))
                elif opcode == 7:  # cdv
                    C = int(A / (2 ** decode(operand)))
            
                instruction_pointer += 2
                
            program_result = ",".join(map(str, output))

            if counter == len(program) - 1:
                if program_result == program_string:
                    new_candidates.append(new_a_octal)
            else:
                if program_string.endswith(program_result):
                    new_candidates.append(new_a_octal)
    candidates = new_candidates
print(int(min(candidates), 8))