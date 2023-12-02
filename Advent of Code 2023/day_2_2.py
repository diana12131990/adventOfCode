import re

class cube:
    def __init__(self,color, number):
        self.color = color
        self.number = number
        
f = open("day_2_input.txt","r")
sum = 0

for line in f:
    bag = [cube("red",0),cube("green",0),cube("blue",0)]
    c_multiply = 1
    
    (game, rounds) = re.split(': ',line)
    cubes = re.split(', |; ',rounds)
    
    for c in cubes:
        (c_num, c_color) = re.split(' ',c)
        c_color = c_color.strip()
        c_cube = cube(c_color,int(c_num))
            
        for b_cube in bag:
            if c_cube.color == b_cube.color and c_cube.number > b_cube.number:
                b_cube.number = c_cube.number
             
    for b_cube in bag:
        c_multiply *= b_cube.number
        
    sum += c_multiply

print(sum)
f.close()