import re

f = open("day_3_input.txt","r")

fabris = [[0]*1000 for _ in range(1000)]


for line in f:
    numbers = [int(n) for n in re.findall(r'\d+',line)]
    for j in range(numbers[1],numbers[1]+numbers[3]):
        for i in range(numbers[2],numbers[2]+numbers[4]):
            fabris[i][j] += 1

print(sum(1 for row in fabris for num in row if num >= 2))