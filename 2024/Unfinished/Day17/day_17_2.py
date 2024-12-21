
program = [2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0]
# B = A%8
# B ^= 1
# C = int(A/2**B)
# B ^= C
# A = int(A/8)
# B ^= C
# output B%8
# if A!=0, restart -> Need to run 16 times to get enough output but no more than 17

for test_A in range(8**15,8**16):
    A = test_A
    B = 0
    C = 0
    output = []
    output_index = 0
    instruction_pointer = 0    
    
    def decode(combo_operand):
        if combo_operand < 4:
            return combo_operand 
        elif combo_operand == 4:
            return A
        elif combo_operand == 5:
            return B
        elif combo_operand == 6:
            return C    
    
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
            new_output = decode(operand) % 8
            if new_output == program[output_index]:
                output.append(new_output)
                output_index += 1
            else:
                break
        elif opcode == 6:  # bdv
            B = int(A / (2 ** decode(operand)))
        elif opcode == 7:  # cdv
            C = int(A / (2 ** decode(operand)))
            
        instruction_pointer += 2
    
    print(test_A,output)
    if output == program:
        print("Done")
        break