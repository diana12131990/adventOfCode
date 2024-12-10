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

distinct_molecules = set()
for from_mol, to_mol in replacements:
    start_index = 0
    while start_index != -1:
        start_index = line.find(from_mol, start_index)
        if start_index != -1:
            end_index = start_index + len(from_mol)
            new_molecule = line[:start_index] + to_mol + line[end_index:]
            distinct_molecules.add(new_molecule)
            start_index += 1         
            
print(len(distinct_molecules)) 