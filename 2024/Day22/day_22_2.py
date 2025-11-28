import re
from collections import defaultdict

f = open("day_22_input.txt","r")

def mix(number, value):
    return number ^ value

def prune(number):
    return number % 16777216

i = 0
sequences = defaultdict(dict)
for n in f:
    n = int(n.strip())
    sequence = []
    prev = int(str(n)[-1])    
    for _ in range(2000):
        n = mix(n,n*64)
        n = prune(n)
        
        n = mix(n,n//32)
        n = prune(n)
        
        n = mix(n,n*2048)
        n = prune(n)
        
        
        current = int(str(n)[-1])
        
        # update 4 length sequence
        sequence.append(current - prev)
        if len(sequence) > 4:
            sequence.pop(0)
        prev = current

        # add sequence to map
        sequence_map = sequences[tuple(sequence)]
        if i not in sequence_map:
            sequence_map[i] = current
    i += 1
f.close()

print(max([sum(results.values()) for results in sequences.values()]))