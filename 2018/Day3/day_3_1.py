import re

fabris = [[0]*1000 for _ in range(1000)]

f = open("day_3_input.txt","r")
for line in f:
    numbers = [int(n) for n in re.findall(r'\d+',line)]
    print(numbers)
    for j in range(numbers[1],numbers[1]+numbers[3]):
        for i in range(numbers[2],numbers[2]+numbers[4]):
            fabris[i][j] += 1
f.close()

print(sum(1 for row in fabris for num in row if num >= 2))