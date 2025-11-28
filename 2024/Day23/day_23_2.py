import re
from collections import defaultdict

f = open("day_23_input.txt","r")

# Prepare the graph
graph = defaultdict(list)

for line in f:
    line = line.strip()
    node1, node2 = line.split('-')
    graph[node1].append(node2)
    graph[node2].append(node1)  
f.close()

def find_largest_connections(remaining, excluded=set(), current_connections=set()):
    if len(remaining) == 0 and len(excluded) == 0 and len(current_connections) > 2:
        return inter_connections.append(tuple(sorted(current_connections)))
    for computer in remaining.copy():
        find_largest_connections(
            remaining.intersection(graph[computer]),
            excluded.intersection(graph[computer]),
            current_connections.union([computer]),
        )
        remaining.remove(computer)
        excluded.add(computer)

inter_connections = []
find_largest_connections(set(graph.keys()))
inter_connections.sort(reverse=True, key=lambda connections: len(connections))
print(','.join(inter_connections[0]))