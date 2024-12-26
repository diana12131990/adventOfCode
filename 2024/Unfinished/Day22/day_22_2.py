import re
import itertools

f = open("day_22_input.txt","r")

def mix(number, value):
    return number ^ value

def prune(number):
    return number % 16777216

price_changes_lists = []
for n in f:
    n = int(n.strip())
    price = n %10
    for _ in range(2000):
        n = mix(n,n*64)
        n = prune(n)
        
        n = mix(n,n//32)
        n = prune(n)
        
        n = mix(n,n*2048)
        n = prune(n)
        
        rate = n%10 - price
        price = n%10
        price_changes_lists.append([(price,rate)])
f.close()

price_changes_set = set(itertools.chain.from_iterable(price_changes_lists))
max_bananas = -1
max_seq = None

for seq in itertools.permutations(price_changes_set, 4):
    bananas = 0
    for price_changes in price_changes_lists:
        for i, val in enumerate(price_changes):
            if i+3 < len(price_changes) and tuple(price_changes[i:i+4]) == seq:
                bananas += prices[i+4]  # i+4 gives us the price after the sequence
                break  # Move on to next buyer
    if bananas > max_bananas:
        max_bananas = bananas
        max_seq = seq

print(f"Optimal price change sequence: {max_seq}, yields {max_bananas} bananas.")