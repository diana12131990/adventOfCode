
steps = 380
insertions = 50000000

curr_pos = 0
after_zero = None

for i in range(1, insertions + 1):
    curr_pos = ((curr_pos + steps) % i) + 1
    if curr_pos == 1:
        after_zero = i
        
print(after_zero) 