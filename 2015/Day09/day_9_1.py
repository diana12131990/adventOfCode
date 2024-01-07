import re
from itertools import permutations

f = open("day_9_input.txt","r")

world_map = {}
worlds = []
for line in f:
    line = line.strip()
    ws,distance = re.split(" = ",line)
    distance = int(distance)
    
    w1,w2 = re.split(" to ",ws)
    if not world_map.has_key(w1):
        world_map.update({w1:{}})
    world_map[w1].update({w2:distance})
    if w1 not in worlds:
        worlds.append(w1)
        
    if not world_map.has_key(w2):
        world_map.update({w2:{}})
    world_map[w2].update({w1:distance})   
    if w2 not in worlds:
        worlds.append(w2)
f.close()

routines = list(permutations(worlds))
min_distance = -1
for r in routines:
    #print(r)
    current_distance = 0
    current_city = ""
    for next_city in r:
        if current_city != "":
            current_distance += world_map[current_city][next_city]
        current_city = next_city
    #print(current_distance)
    if min_distance == -1 or min_distance > current_distance:
        min_distance = current_distance

print(min_distance)