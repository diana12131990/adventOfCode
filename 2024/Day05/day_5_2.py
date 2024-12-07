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
            i = 0
            correct = True
            while i < len(rules):
                rule = rules[i]
                if rule[0] in pages and rule[1] in pages:
                    i1 = pages.index(rule[0])
                    i2 = pages.index(rule[1])
                    if i1 > i2:
                        correct = False
                        pages[i1], pages[i2] = pages[i2], pages[i1]
                        i = 0
                    else:
                        i += 1
                else:
                    i += 1
            if not correct:
                total += int(pages[len(pages)//2])

f.close()

print(total)