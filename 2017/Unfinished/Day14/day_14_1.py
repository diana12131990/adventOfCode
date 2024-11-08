import re
import hashlib

hash_input = "flqrgnkx"+"-"

def convert_string_to_32hex(string):
    return hashlib.sha256(string.encode()).hexdigest()[:32]

def convert_string_to_binary(string):
    return bin(int(string,16))[2:].zfill(len(string)*4)

def change_binary_representation(string):
    temp_string = string.replace('0','.')
    final_string = temp_string.replace('1','#')

total_used = 0

test = 'a0c2017'
print(convert_string_to_binary(test))

for n in range(128):
    hash_string = hash_input + str(n)
    print(hash_string)
    output = convert_string_to_32hex(hash_string)
    bits = str(convert_string_to_binary(output))
    print(bits)
    print(change_binary_representation(bits))
    total_used += bits.count('1')
        
print(total_used)