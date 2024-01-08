from itertools import groupby

line = "1113222113"

for i in range(50):
    
    new_line = ""
    for key, group in groupby(line):
        length = len(list(group))
        new_line += str(length) + key
        
    line = new_line

print(len(line))