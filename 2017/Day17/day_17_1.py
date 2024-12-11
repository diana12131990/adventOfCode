
steps = 380
insertions = 2017

buffer = [0]  # Initialize buffer with 0
curr_pos = 0  # Current position is 0 index
for i in range(1, insertions + 1):
    curr_pos = (curr_pos + steps) % len(buffer)  # Current position after steps
    buffer.insert(curr_pos + 1, i)  # Insert new value
    curr_pos += 1  # Move current position to new value

print(buffer[(buffer.index(insertions) + 1) % len(buffer)]) 