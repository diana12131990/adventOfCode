import re

f = open("day_5_input.txt","r")

rules = []
reading_rule = True
total = 0
for line in f:
    line = line.strip()
    if line == "":
        reading_rule = False
    else:
        pages = re.findall(r'\d+', line)
        if reading_rule:
            rules.append(pages)
        else:
            correct = True
            for rule in rules:
                if rule[0] in pages and rule[1] in pages:
                    if pages.index(rule[0]) > pages.index(rule[1]):
                        correct = False
                        break
            if correct:
                total += int(pages[len(pages)//2])

f.close()

print(total)