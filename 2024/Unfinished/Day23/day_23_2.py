import re
from collections import defaultdict
from itertools import combinations

f = open("day_23_input.txt","r")

graph = defaultdict(list)
for line in f:
    line = line.strip()
    node1, node2 = line.split('-')
    graph[node1].append(node2)
    graph[node2].append(node1)  
f.close()

def find_largest_clique(graph):
    nodes = set(graph.keys())
    clique_sizes = range(len(nodes), 2, -1)  # Decreasing order of size, skip size 1
    for size in clique_sizes:
        for candidate_clique_nodes in combinations(nodes, size):
            if all(pair_of_nodes_are_connected(pair, graph) for pair in combinations(candidate_clique_nodes, 2)):
                return sorted(candidate_clique_nodes)

def pair_of_nodes_are_connected(pair, graph):
    return pair[1] in graph[pair[0]]

# Find the largest clique
largest_clique = find_largest_clique(graph)

# Generate the password
password = ','.join(largest_clique)

print(password)