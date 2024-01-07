import re

def GetCup(l_index,l,combination):
    current_liter = l
    for x in range(l_index+1,len(cups)):
        current_liter += cups[x]
        used.append(cups[x])
        if current_liter == total_liter:
            combination += 1  
            print(used)
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
Found = False 
i = -1

combination = GetCup(-1,0,0)
        
'''for a in range(len(cups)):
    current_liter += cups[a]
    if current_liter == total_liter:
        combination += 1
        print(cups[a])
    elif current_liter < total_liter:
        for b in range(a+1,len(cups)):
            current_liter += cups[b]
            if current_liter == total_liter:
                combination += 1
                print(cups[a],cups[b])
            elif current_liter < total_liter:
                for c in range(b+1,len(cups)):
                    current_liter += cups[c]
                    if current_liter == total_liter:
                        combination += 1
                        print(cups[a],cups[b],cups[c])   
                    elif current_liter < total_liter:
                        for d in range(c+1,len(cups)):
                            current_liter += cups[d]
                            if current_liter == total_liter:
                                combination += 1
                                print(cups[a],cups[b],cups[c])   
                            elif current_liter < total_liter:
                                print("Need More")
                            current_liter -= cups[d]
                    current_liter -= cups[c]
            current_liter -= cups[b]
    current_liter -= cups[a]'''
print(combination)