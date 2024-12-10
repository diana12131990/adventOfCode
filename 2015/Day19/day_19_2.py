import re

f = open("day_19_input.txt","r")

replacements = []
medicine_molecule = ""
GetReplacement = True
for line in f:
    if line == "\n":
        GetReplacement = False
    else:
        line = line.strip()
        if GetReplacement:
            from_mol, to_mol = line.split(' => ')
            replacements.append((from_mol, to_mol))
        else:
            medicine_molecule = line
f.close()

replacements.sort(key = lambda x: len(x[1]), reverse=True)   # sort by length of "to" molecule
steps = 0
while medicine_molecule != 'e':
    for from_mol, to_mol in replacements:
        if to_mol in medicine_molecule:
            medicine_molecule = medicine_molecule.replace(to_mol, from_mol, 1)    # replace only the first occurrence
            steps += 1
            
print(steps) 