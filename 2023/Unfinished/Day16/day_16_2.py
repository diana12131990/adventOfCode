import re
import copy
import sys
sys.setrecursionlimit(10000)

f = open("day_16_input.txt","r")
o_laser_map = []
o_energy_map = []
laser_map = []
energy_map = [] 
for line in f:
    line = line.strip()
    o_laser_map.append([x for x in line])
    o_energy_map.append(["."]*len(o_laser_map[0]))
f.close()

def RunLaser(i,j,direction):
    if 0<= i < len(laser_map) and 0<= j < len(laser_map[0]):
        energy_map[i][j] = "#"
        if laser_map[i][j] == "/":
            if direction == "Right":
                RunLaser(i-1,j,"Up")
            elif direction == "Left":
                RunLaser(i+1,j,"Down")
            elif direction == "Up":
                RunLaser(i,j+1,"Right")
            elif direction == "Down":
                RunLaser(i,j-1,"Left") 
        
        elif laser_map[i][j] == "\\":
            if direction == "Right":
                RunLaser(i+1,j,"Down")
            elif direction == "Left":
                RunLaser(i-1,j,"Up")                
            elif direction == "Up":
                RunLaser(i,j-1,"Left")                  
            elif direction == "Down":
                RunLaser(i,j+1,"Right")
                
        elif laser_map[i][j] == "|":
            if direction == "Right" or direction == "Left":
                RunLaser(i+1,j,"Down")
                RunLaser(i-1,j,"Up")
            elif direction == "Up":
                RunLaser(i-1,j,direction)                  
            elif direction == "Down":
                RunLaser(i+1,j,direction)

        elif laser_map[i][j] == "-":
            if direction == "Down" or direction == "Up":
                RunLaser(i,j-1,"Left")
                RunLaser(i,j+1,"Right")
            elif direction == "Left":
                RunLaser(i,j-1,direction)                  
            elif direction == "Right":
                RunLaser(i,j+1,direction)
        
        else:
            if direction == "Right":
                if laser_map[i][j] == ".":
                    laser_map[i][j] = ">"
                    RunLaser(i,j+1,direction)
                elif laser_map[i][j] == "^" or laser_map[i][j] == "v":
                    laser_map[i][j] = "2"
                    RunLaser(i,j+1,direction)
                    
            elif direction == "Left":
                if laser_map[i][j] == ".":
                    laser_map[i][j] = "<"
                    RunLaser(i,j-1,direction)
                elif laser_map[i][j] == "^" or laser_map[i][j] == "v":
                    laser_map[i][j] = "2"
                    RunLaser(i,j-1,direction)

            elif direction == "Up":
                if laser_map[i][j] == ".":
                    laser_map[i][j] = "^"
                    RunLaser(i-1,j,direction)
                elif laser_map[i][j] == ">" or laser_map[i][j] == "<":
                    laser_map[i][j] = "2"
                    RunLaser(i-1,j,direction)
                    
            elif direction == "Down":
                if laser_map[i][j] == ".":
                    laser_map[i][j] = "v"
                    RunLaser(i+1,j,direction) 
                elif laser_map[i][j] == ">" or laser_map[i][j] == "<":
                    laser_map[i][j] = "2" 
                    RunLaser(i+1,j,direction) 

def countEnergy(max_energy,energy_map):
    total_energized = 0
    for x in energy_map:
        total_energized += x.count("#")
    if max_energy < total_energized:
        return total_energized
    else:
        return max_energy
    
max_energy = 0
for i in range(len(o_laser_map[0])):
    laser_map = copy.deepcopy(o_laser_map)
    energy_map = copy.deepcopy(o_energy_map) 
    RunLaser(0,i,"Down")
    max_energy = countEnergy(max_energy, energy_map)

for i in range(len(o_laser_map[0])):   
    laser_map = copy.deepcopy(o_laser_map)
    energy_map = copy.deepcopy(o_energy_map)      
    RunLaser(len(o_laser_map),i,"Up")
    max_energy = countEnergy(max_energy, energy_map)

for i in range(len(o_laser_map)):
    laser_map = copy.deepcopy(o_laser_map)
    energy_map = copy.deepcopy(o_energy_map)   
    RunLaser(i,0,"Right")
    max_energy = countEnergy(max_energy, energy_map)
    
for i in range(len(o_laser_map)):
    laser_map = copy.deepcopy(o_laser_map)
    energy_map = copy.deepcopy(o_energy_map)   
    RunLaser(i,len(o_laser_map[0]),"Left")
    max_energy = countEnergy(max_energy, energy_map)

print(max_energy)    
