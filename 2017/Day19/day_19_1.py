import re

p_map = {}
i = 0
j = -1
p_dir = "Down"
letters = ""

def FindDirection(letters,c_dir,n_pipe):
    if n_pipe.isalpha():
        letters += n_pipe
        
    elif n_pipe == "+":
        if c_dir == "Down" or c_dir == "Up":
            if j != 0:
                if p_map[i][j-1] != " " and p_map[i][j-1] != "|":
                    return (letters,"Left")
                
            if j-1 < len(p_map[0]):
                if p_map[i][j+1] != " " and p_map[i][j+1] != "|":
                    return (letters,"Right")
        elif c_dir == "Left" or c_dir =="Right":
            if i != 0:
                if p_map[i-1][j] != " " and p_map[i-1][j] != "-":
                    return (letters,"Up")
            if i-1 < row:
                if p_map[i+1][j] != " " and p_map[i+1][j] != "-":
                    return (letters,"Down")
    
    return (letters,c_dir)

f = open("day_19_input.txt","r")

row = 0
for line in f:
    line = line.replace("\n","")
    line = [x for x in line]
    line = line[1:-1]
    p_map.update({row:line})
    if row == 0:
        j = line.index("|")
    row += 1
f.close()

while True:
    if p_dir == "Up":
        i -= 1
    elif p_dir == "Down":
        i += 1           
    elif p_dir == "Left":
        j -= 1
    elif p_dir == "Right":
        j += 1
        
    if i < 0 or i == row or j < 0 or j == len(p_map[0]) or p_map[i][j] == " ":
        break
    
    (letters,p_dir) = FindDirection(letters,p_dir,p_map[i][j])
    
print(letters)