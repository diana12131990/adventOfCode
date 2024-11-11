import re

f = open("day_3_test_input.txt","r")

fabris = [[None]*8 for _ in range(8)]

elf_list = []

for line in f:
    numbers = [int(n) for n in re.findall(r'\d+',line)]
    elf_list.append[True];
    for j in range(numbers[1],numbers[1]+numbers[3]):
        for i in range(numbers[2],numbers[2]+numbers[4]):
            if not fabris[i][j]:
                fabris[i][j] = [numbers[0]]
            else:
                fabris[i][j].append(numbers[0])


    for line in fabris:
        print(line)