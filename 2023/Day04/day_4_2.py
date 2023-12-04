import re

f = open("day_4_input.txt","r")
match_counts = []
copies = []
total_copies = 0

for line in f:
    game, cards = re.split(': ',line)
    win_numbers, self_numbers = re.split(' \| ',cards)
    win_numbers = re.findall('\d+',win_numbers)
    self_numbers = re.findall('\d+',self_numbers)
    match_numbers = list(set(win_numbers) & set(self_numbers))
    match_counts.append(len(match_numbers))
    copies.append(1)

for i in range(len(match_counts)):
    for c in range(copies[i]):
        for j in range(match_counts[i]):
            copies[i+j+1] += 1      

total_copies = sum(copies)        

print(total_copies)    
f.close()