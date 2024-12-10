import re

def process_nodes(data):
    child_nodes_count, metadata_entries_count = data[:2]
    data = data[2:]

    total = 0
    for _ in range(child_nodes_count):
        total_child, data = process_nodes(data)
        total += total_child

    metadata_entries = data[:metadata_entries_count]
    total += sum(metadata_entries)

    return total, data[metadata_entries_count:]

f = open("day_8_input.txt","r")
line = f.readline()
nodes = list(map(int, line.split()))
f.close()

total, _ = process_nodes(nodes)

print(total)