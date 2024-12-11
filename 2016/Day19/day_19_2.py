elf_amount = 3014603

p = 1
while 3*p <= elf_amount:
    p *= 3
if elf_amount-p <= p: # elf_amount <= 2*p
    print(elf_amount-p)
else:
    print(elf_amount-p + max(elf_amount-2*p, 0)) # elf_amount > 2*p

