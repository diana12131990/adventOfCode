
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
def find_path(node, path):
    path.append(node)
    
    if node == "out":
        all_paths.append(list(path))
    elif node in data:
        for next_node in data[node]:
            find_path(next_node, path)
    path.pop()

find_path("you",[])

print(len(all_paths))