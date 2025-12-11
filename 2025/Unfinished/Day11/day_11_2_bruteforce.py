
import re

f = open("day_11_input.txt","r")

data = {}
for line in f:
    line = line.strip()
    name, outputs = line.split(":")
    outputs = outputs[1:].split(" ")
    data[name] = outputs
f.close()

all_paths = []
required_nodes = {"dac","fft"}
def find_path(node, path, visited_in_path, found_required_nodes):
    path.append(node)
    visited_in_path.add(node)
    
    if node in required_nodes:
        found_required_nodes.add(node)
    
    if node == "out":
        if found_required_nodes == required_nodes:
            all_paths.append(list(path))
    elif node in data:
        for next_node in data[node]:
            if next_node not in visited_in_path:
                find_path(next_node, path, visited_in_path, set(found_required_nodes))
    path.pop()
    visited_in_path.remove(node)

find_path("svr",[],set(),set())

print(len(all_paths))