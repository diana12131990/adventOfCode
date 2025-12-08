
import re
import math
    
# Find the root of the set containing box i
def find_root(parent,i):
    if parent[i] == i:
        return i
    parent[i] = find_root(parent, parent[i])
    return parent[i]


f = open("day_8_input.txt","r")

junction_boxes = []
for line in f:
    line = line.strip()
    x,y,z = map(int,line.split(","))
    junction_boxes.append([x,y,z])
f.close()

connections = []
total_boxes = len(junction_boxes)

# Get all the distances between two boxes and sort
for i in range(total_boxes):
    for j in range(i+1,total_boxes):
        dist = math.sqrt((junction_boxes[i][0] - junction_boxes[j][0])**2 
                         + (junction_boxes[i][1] - junction_boxes[j][1])**2
                         + (junction_boxes[i][2] - junction_boxes[j][2])**2)
        connections.append((dist,i,j))
connections.sort()

# Each box is their own parent initially
unionData_parent = list(range(total_boxes))
# Each set has 1 box/size 1 initially
unionData_size = [1] * total_boxes

# Union boxes
for k in range(1000):
    dist,i,j = connections[k]
    
    root_i = find_root(unionData_parent,i)
    root_j = find_root(unionData_parent,j)
    
    #print(i,j,root_i,root_j)
    
    if root_i != root_j:
        if unionData_size[root_i] < unionData_size[root_j]:
            root_i,root_j = root_j,root_i
        unionData_parent[root_j] = root_i
        unionData_size[root_i] += unionData_size[root_j]
        
    #print(unionData_parent)
    #print(unionData_size)

# Get circuit size
circuit_size = []
for i in range(total_boxes):
    if unionData_parent[i] == i:
        circuit_size.append(unionData_size[i])
circuit_size.sort(reverse=True)

print(math.prod(circuit_size[:3]))