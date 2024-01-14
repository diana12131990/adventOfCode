elf_amount = 3014603

elfs = []
for i in range(1,elf_amount+1):
    if i%2 == 1:
        if i == elf_amount:
            elfs.append([i,1])
        else:
            elfs.append([i,2])

i = len(elfs)-1
while len(elfs) != 1:
    j = i+1
    if j == len(elfs):
        j = 0
    elfs[i][1] += elfs[j][1]
    elfs.pop(j)
    i = j
    if i == len(elfs):
        i = 0
    if i == 0:
        print(elfs)
print(elfs[0][0])