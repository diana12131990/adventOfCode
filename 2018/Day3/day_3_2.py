import re

fabris = [[None]*1000 for _ in range(1000)]

elf_fabric = [False]

f = open("day_3_input.txt","r")
for line in f:
    numbers = [int(n) for n in re.findall(r'\d+',line)]
    elf_fabric.append(True)
    for j in range(numbers[1],numbers[1]+numbers[3]):
        for i in range(numbers[2],numbers[2]+numbers[4]):
            if not fabris[i][j]:
                fabris[i][j] = [numbers[0]]
            else:
                fabris[i][j].append(numbers[0])
            
            if len(fabris[i][j])>1:
                for n in fabris[i][j]:
                    if elf_fabric[int(n)]:
                        elf_fabric[int(n)] = False
f.close()

print(elf_fabric.index(True))