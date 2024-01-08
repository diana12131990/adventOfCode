import re

Stores = {
    "Weapon":[],
    "Armor":[],
    "Ring":[]
}

player = {
    "Hit Point": 100,
    "Damage": 0,
    "Armor": 0
}

enemy = {
    "Hit Point": 103,
    "Damage": 9,
    "Armor": 2
}

def CauseDamage(attacker_damage, defender_armor, defender_health):
    damage = attacker_damage - defender_armor
    if damage <= 0:
        damage = 1
    return defender_health - damage
    

def PlayerWin(attack,defense):
    p = player.copy()
    e = enemy.copy()
    p["Damage"] += attack
    p["Armor"] += defense
    while True:
        e["Hit Point"] = CauseDamage(p["Damage"], e["Armor"], e["Hit Point"])
        if e["Hit Point"] <= 0:
            return True
        p["Hit Point"] = CauseDamage(e["Damage"], p["Armor"], p["Hit Point"])
        if p["Hit Point"] <= 0:
            return False        

f = open("day_21_input.txt","r")
for line in f:
    line = line.strip()
    if "Weapons" in line:
        category = "Weapon"
    elif "Rings" in line:
        category = "Ring"
    elif "Armor" in line:
        category = "Armor"        
    elif line != "":
        data = re.findall("\d+",line)
        Stores[category].append([int(data[-3]),int(data[-2]),int(data[-1])])
f.close()

ring_amount = len(Stores["Ring"])
two_ring_order = []
for i in range(ring_amount):
    for j in range(i+1,ring_amount):
        two_ring_order.append([i,j])

min_cost = -1
for w in Stores["Weapon"]:
    cost = w[0]
    item = [["Weapon",w[0]]]
    player["Damage"] = w[1]
    
    for i in range(-1,len(Stores["Armor"])):
        p_attack = 0
        p_defende = 0
        if i != -1:
            a = Stores["Armor"][i]
            cost += a[0]
            item.append(["Armor",a[0]])
            p_defende += a[2]
            
        for ring_amount in range(3):
            if ring_amount == 0:
                if PlayerWin(p_attack, p_defende):
                    if min_cost == -1 or min_cost > cost:
                        min_cost = cost
                    break
            elif ring_amount == 1:
                for j in range(len(Stores["Ring"])):
                    r = Stores["Ring"][j]
                    cost += r[0]
                    item.append(["Ring",r[0]])
                    p_attack += r[1]
                    p_defende += r[2]
                    
                    if PlayerWin(p_attack, p_defende):
                        if min_cost == -1 or min_cost > cost:
                            min_cost = cost   
                            
                    cost -= r[0]
                    item.pop(-1)
                    p_attack -= r[1]
                    p_defende -= r[2]
            else:
                for j in two_ring_order:
                    r1 = Stores["Ring"][j[0]]
                    cost += r1[0]
                    item.append(["Ring",r1[0]])
                    p_attack += r1[1]
                    p_defende += r1[2]
                    
                    r2 = Stores["Ring"][j[1]]
                    item.append(["Ring",r2[0]])
                    cost += r2[0]
                    p_attack += r2[1]
                    p_defende += r2[2]      
                    
                    if PlayerWin(p_attack, p_defende):
                        if min_cost == -1 or min_cost > cost:
                            min_cost = cost  
                            
                    cost -= r1[0]
                    item.pop(-1)
                    p_attack -= r1[1]
                    p_defende -= r1[2]                    
                    cost -= r2[0]
                    item.pop(-1)
                    p_attack -= r2[1]
                    p_defende -= r2[2]                     
        if i != -1:
            cost = w[0]
            item.pop(-1)
            
print(min_cost)