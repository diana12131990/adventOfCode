

player = {
    "HP": 50,
    "MP": 500
}

enemy = {
    "HP": 71,
    "Damage": 10
}

Magic = [    # 0: Cost, 1:Turn, 2:+HP, 3:+Damage, 4:+Armor, 5:+MP, 6: active
    [53,1,0,4,0,0,True],     # Missle
    [73,1,2,2,0,0,True],     # Drain
    [113,6,0,0,7,0,False],   # Shield
    [173,6,0,3,0,0,False],   # Poison
    [229,5,0,0,0,101,False]  # Recharge
]

def CauseDamage(attacker_damage, defender_armor, defender_health):
    damage = attacker_damage - defender_armor
    if damage <= 0:
        damage = 1
    return defender_health - damage

def PlayerWin(p,e,magics):
    p_damage = 0
    
    # player turn
    i = 0
    while i != len(magics):
        if magics[i][6]:
            m = magics[i]
            p["HP"] += m[2]
            p_damage += m[3]
            p["MP"] += m[5]
            
            magics[i][1] -= 1
            if m[1] == 0:
                magics.pop(i)
            else:
                i += 1
        else:
            magics[i][6] = True
            i += 1
    e["HP"] = CauseDamage(p_damage, 0, e["HP"])
    if e["HP"] <= 0:
        return 1
    
    p_armor = 0
    # enemy turn
    i = 0
    while i != len(magics):
        m = magics[i]
        p["HP"] += m[2]
        p_armor += m[4]
        p["MP"] += m[5]
        
        magics[i][1] -= 1
        if magics[i][1] == 0:
            magics.pop(i)
        else:
            i += 1    
    p["HP"] = CauseDamage(e["Damage"], p_armor, p["HP"])
    if p["HP"] <= 0:
        return 0
    
    return -1

def Battle(p,e,magics,mp_cost):
    i = 0
    
    if p["MP"] < Magic[i][0]:
        return -1
    # else

MP_cost = Battle(player,enemy,[],0)