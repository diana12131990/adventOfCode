import re
from itertools import combinations

f = open("day_24_input.txt","r")
gifts = []

for line in f:
    line = line.strip()
    
    gifts.append(int(line))
f.close()

weight = sum(gifts)/4
solutions = []

Found = False
min_package = 1
while min_package != len(gifts):
    for c in combinations(gifts,min_package):
        if sum(c) == weight:
            solutions.append(list(c))
            Found = True
    if Found:
        break
    else:
        min_package += 1
    
    
def Product(l):
    num = 1
    for x in l:
        num *= x
    return num

min_QE = -1
for x in solutions:
    c_QE = Product(x)
    if min_QE == -1 or min_QE > c_QE:
        min_QE = c_QE    
print(min_QE)