import re

def process_nodes(data):
    child_nodes_count, metadata_entries_count = data[:2]
    data = data[2:]

    child_values = []
    for _ in range(child_nodes_count):
        child_value, data = process_nodes(data)
        child_values.append(child_value)

    metadata_entries = data[:metadata_entries_count]
    data = data[metadata_entries_count:]

    if child_nodes_count == 0:
        return sum(metadata_entries), data

    value = 0
    for entry in metadata_entries:
        # Adjust for 1-indexing
        if entry - 1 < len(child_values):
            value += child_values[entry - 1]

    return value, data

f = open("day_8_input.txt","r")
line = f.readline()
nodes = list(map(int, line.split()))
f.close()

root_value, _ = process_nodes(nodes)

print(root_value)