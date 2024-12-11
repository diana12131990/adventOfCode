import re

stones = "872027 227 18 9760 0 4 67716 9245696"
stones = re.findall(r'\d+', stones)

total_blink_time = 75

# This will mutate a given stone number as per the rules. Do it math style for speed.
def Change(stone):
    if stone == '0':
        return ['1']
    elif len(stone)%2 == 0:
        splitN = len(stone)//2
        s1 = str(int(stone[:splitN]))
        s2 = str(int(stone[splitN:]))    
        return [s1,s2]
    else:
        return [str(int(stone)*2024)]

stone_dict = {}
for s in stones:
    stone_dict.update({s:{'next': Change(s), 'history': {x:0 for x in range(total_blink_time+1)}}})
    stone_dict[s]['history'][0] = 1

GetAllStone = False
while not GetAllStone:
    GetAllStone = True
    check_list = stone_dict.copy()
    for stones in check_list.values():
        for s in stones['next']:
            if s not in stone_dict:
                GetAllStone = False
                stone_dict.update({s:{'next': Change(s), 'history': {x:0 for x in range(total_blink_time+1)}}})


# record how many times each one appears at each blink
for time in range(total_blink_time):
    previous_stones = {}
    for stone, info in stone_dict.items():
        if info['history'][time] > 0:
            previous_stones.update({stone:info})
    for stone_info in previous_stones.values():
        for stone_num in stone_info['next']:
            stone_dict[stone_num]['history'][time+1] += stone_info['history'][time]
            
            
# Print the number of stones that appear in the data for the final blink!
print(sum([data['history'][total_blink_time] for data in stone_dict.values()]))