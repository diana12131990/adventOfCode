import re

f = open("day_10_input.txt","r")

def GiveChip(source,target,chip):
    bots[source].remove(chip)
    if not bots.has_key(target):
        bots.update({target:[]})
    bots[target].append(chip)
    bots[target] = sorted(bots[target])
    
def OutputChip(source,target,chip):
    bots[source].remove(chip)
    outputs.update({target:chip})

def DetectTag(source,name,chip):
    num = re.findall("\d+",name)
    target = num[0]
    if "bot" in name:
        GiveChip(source, target, chip)
    else:
        OutputChip(source, target, chip)

bots = {}
outputs = {}
actions = []
target_bots = ""
for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    if "value" in line:
        value = int(numbers[0])
        bot_number = numbers[1]
        if not bots.has_key(bot_number):
            bots.update({bot_number:[]})
        bots[bot_number].append(value)
        bots[bot_number] = sorted(bots[bot_number])
    else:
        bot_number = numbers[0]
        source,line = re.split(" gives low to ",line)
        low,high = re.split(" and high to ",line)
        Done = False
        if bots.has_key(bot_number):
            if len(bots[bot_number]) == 2:
                if bots[bot_number] == [17,61]:
                    target_bots = bot_number                
                DetectTag(bot_number, low, bots[bot_number][0])
                DetectTag(bot_number, high, bots[bot_number][0])
                Done = True
        if not Done:
            actions.append([bot_number,low,high])
f.close()

while actions != []:
    line = actions[0]
    bot_number = line[0]
    low = line[1]
    high = line[2]
    Done = False
    if bots.has_key(bot_number):
        if len(bots[bot_number]) == 2:
            if bots[bot_number] == [17,61]:
                target_bots = bot_number
            DetectTag(bot_number, low, bots[bot_number][0])
            DetectTag(bot_number, high, bots[bot_number][0])
            Done = True
    if not Done:
        actions.append(line)    
    actions.pop(0)
  
print(target_bots)