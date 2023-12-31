import re
import sys
sys.setrecursionlimit(10000)

f = open("day_16_input.txt","r")
laser_map = []
energy_map = []
for line in f:
    line = line.strip()
    laser_map.append([x for x in line])
    energy_map.append(["."]*len(laser_map[0]))
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

RunLaser(0,0,"Right")

total_energized = 0
for x in energy_map:
    total_energized += x.count("#")
print(total_energized)