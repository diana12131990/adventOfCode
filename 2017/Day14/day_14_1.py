import re

hash_input = "flqrgnkx"+"-"

total_used = 0
for n in range(128):
    hash_string = hash_input + str(n)
    twist_list = [ord(x) for x in hash_string]
    print(hash_string)

    numbers = [i for i in range(256)]
    skip_size = 0
    i = 0
    for r in range(64):
        for n in twist_list:
            if n != 0:
                i += skip_size
                i = i%256
                j = i+n
                j = j%256
                if j > i:
                    twist = numbers[i:j]
                elif j <= i:
                    twist = numbers[i:]+numbers[:j]
                twist.reverse()
                for index in range(len(twist)):
                    k = i+index
                    k = k%256
                    numbers[k] = twist[index]
                i += n-1
            skip_size += 1
    
    test_string = []
    for x in range(256/16):
        xor_result = -1
        for i in range(16):
            if i == 0:
                xor_result = numbers[i+16*x]
            else:
                xor_result ^= numbers[i+16*x]
        hex_n = hex(xor_result)
        hex_n = hex_n.replace("0x","")
        if len(hex_n)==1:
            hex_n = "0"+hex_n
        for x in hex_n:
            hex_integer = int(x, 16)
            binary_string = format(hex_integer,'b')
            binary_string = "0"*(4-len(binary_string)) + binary_string
            test_string.append(binary_string)
            binary_string = re.findall("\d",binary_string)
            total_used += binary_string.count("1")
    print(''.join(test_string))
print(total_used)