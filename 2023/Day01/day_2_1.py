import re


class cube:
    def __init__(self,color, number):
        self.color = color
        self.number = number
        
f = open("day_2_input.txt","r")
bag = [cube("red",12),cube("green",13),cube("blue",14)]
sum = 0

def CompareCube(game_info):
    
    for item in game_info:
        (c_num, c_color) = re.split(' ',item)
        c_color = c_color.strip()
        c_cube = cube(c_color,int(c_num))
        
        for b_cube in bag:
            if c_cube.color == b_cube.color and c_cube.number > b_cube.number:
                return False
        
    return True 


for line in f:
    (game, rounds) = re.split(': ',line)
    (_,id) = re.split(' ',game)
    cubes = re.split(', |; ',rounds)
    
    if (CompareCube(cubes)):
        sum += int(id)

print(sum)    
f.close()