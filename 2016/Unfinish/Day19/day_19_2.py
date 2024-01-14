elf_amount = 3014603

elfs = []
for i in range(1,elf_amount+1):
    elfs.append([i,1])
    
i = 0
while len(elfs) != 1:
    j = len(elfs)/2 + i
    if j >= len(elfs):
        j -= len(elfs)
    elfs[i][1] += elfs[j][1]
    elfs.pop(j)
    i += 1
    if i >= len(elfs):
        i = 0
        print(elfs)
print(elfs[0][0])