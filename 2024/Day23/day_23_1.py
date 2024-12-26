import re
from collections import defaultdict
from itertools import combinations

f = open("day_23_input.txt","r")

# Prepare the graph
graph = defaultdict(list)

for line in f:
    line = line.strip()
    node1, node2 = line.split('-')
    graph[node1].append(node2)
    graph[node2].append(node1)  
f.close()

# Helper function to check if a triplet of nodes are interconnected
def is_triplet_interconnected(triplet, graph):
    n1, n2, n3 = sorted(triplet)
    # Checking if there is a connection between each pair of computers
    return n2 in graph[n1] and n3 in graph[n1] and n3 in graph[n2]

# Store the results as a list of sets of interconnected nodes
node_triplets = filter(lambda triplet: is_triplet_interconnected(triplet, graph), combinations(graph.keys(), 3))

# Filter for triplets where at least one node starts with 't'
node_triplets_start_t = [triplet for triplet in node_triplets if any(node.startswith('t') for node in triplet)]


print(len(node_triplets_start_t))