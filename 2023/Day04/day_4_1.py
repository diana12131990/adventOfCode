import re

f = open("day_4_input.txt","r")
sum = 0

for line in f:
    game, cards = re.split(': ',line)
    win_numbers, self_numbers = re.split(' \| ',cards)
    win_numbers = re.findall('\d+',win_numbers)
    self_numbers = re.findall('\d+',self_numbers)
    match_numbers = list(set(win_numbers) & set(self_numbers))
    
    game_point = 0
    last_point = 0
    for i in range(len(match_numbers)):
        if last_point == 0:
            game_point = 1
        else:
            game_point = last_point*2
        last_point = game_point
    sum += game_point


print(sum)    
f.close()