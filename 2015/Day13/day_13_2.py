import re
from itertools import permutations

def GetRelation(happiness):
    num = re.findall("\d+",happiness)
    if "gain" in happiness:
        return int(num[0])
    elif "lose" in happiness:
        return -1 * int(num[0])

f = open("day_13_input.txt","r")

relation = {}
names= []
for line in f:
    line = line.strip()
    p1,line = re.split(" would ",line)
    happiness,p2 = re.split(" happiness units by sitting next to ",line)
    p2 = p2.replace(".","")
    
    if not relation.has_key(p1):
        relation.update({p1:{}})
    relation[p1].update({p2:GetRelation(happiness)})
    if p1 not in names:
        names.append(p1)
f.close()

relation.update({"me":{}})
for p in names:
    relation["me"].update({p:0})
    relation[p].update({"me":0})
names.append("me")

print(relation)
print(names)

seats = list(permutations(names))
max_happiness = -1
for order in seats:
    current_happiness = 0
    for i in range(len(order)):
        p = order[i]
        if i-1 < 0:
            l_p = order[-1]
        else:
            l_p = order[i-1]
        if i+1 == len(order):
            r_p = order[0]
        else:
            r_p = order[i+1]
        current_happiness += relation[p][l_p] + relation[p][r_p]
    if current_happiness > max_happiness:
        max_happiness = current_happiness

print(max_happiness)