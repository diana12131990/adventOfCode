def knot_hash(input):
    lengths = [ord(ch) for ch in input] + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    position = 0
    skip_size = 0
    for _ in range(64):
        for length in lengths:
            if length > 1:
                numbers = numbers[position:] + numbers[:position]
                numbers[:length] = reversed(numbers[:length])
                numbers = numbers[-position:] + numbers[:-position]
            position = (position + length + skip_size) % 256
            skip_size += 1
    dense = [0]*16
    for i in range(16):
        for j in range(16):
            dense[i] ^= numbers[i*16+j]
    return "".join(f"{i:02x}" for i in dense)

key_str = "hxtvlmkl"

total_used = 0
for i in range(128):
    s = f"{key_str}-{i}"
    knot_hash_string = knot_hash(s)
    binary_hash = bin(int(knot_hash_string, 16))[2:].zfill(128)
    total_used += binary_hash.count('1')

print(total_used)