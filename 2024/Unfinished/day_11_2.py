import re

stones = "872027 227 18 9760 0 4 67716 9245696"
stones = re.findall(r'\d+', stones)

for time in range(75):
    i = 0
    while i < len(stones):
        if stones[i] == '0':
            stones[i] = '1'
        elif len(stones[i])%2 == 0:
            splitN = len(stones[i])//2
            s1 = str(int(stones[i][:splitN]))
            s2 = str(int(stones[i][splitN:]))
            stones[i] = s1
            i += 1
            stones.insert(i,s2)    
        else:
            stones[i] = str(int(stones[i])*2024)
        i += 1
    print(time,len(stones))