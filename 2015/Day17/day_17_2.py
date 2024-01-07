import re

def GetCup(l_index,l,combination):
    current_liter = l
    for x in range(l_index+1,len(cups)):
        current_liter += cups[x]
        used.append(cups[x])
        if current_liter == total_liter:
            combination += 1  
            # print(used)
            combination_amount.append(len(used))
        elif current_liter < total_liter:
            combination = GetCup(x,current_liter,combination)
        current_liter -= cups[x]
        used.pop(-1)
    return combination

f = open("day_17_input.txt","r")

cups = []

for line in f:
    line = line.strip()
    
    cups.append(int(line))
f.close()

total_liter = 150
combination = 0
current_liter = 0
used = []
combination_amount = []
Found = False 
i = -1

combination = GetCup(-1,0,0)

min_cups = combination_amount[0]
min_combination = 0
for x in combination_amount:
    if x == min_cups:
        min_combination += 1
    elif x < min_cups:
        min_cups = x
        min_combination = 1

print(min_combination)