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

# Add stone file from the input first, and make their history 0 (init) to have 1
for s in stones:
    stone_dict.update({s:{'next': Change(s), 'history': {x:0 for x in range(total_blink_time+1)}}})
    stone_dict[s]['history'][0] = 1

# Add all the other stone that might be created in the future into the dictionary
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
    # If the stone show in this round
    # find their result in the next run
    # add the this round's stone amount of number to the next round
    for info in stone_dict.values():
        if info['history'][time] > 0:
            for s in info['next']:
                stone_dict[s]['history'][time+1] += info['history'][time]

total_stone = 0
for data in stone_dict.values():
    total_stone += data['history'][total_blink_time]
print(total_stone)