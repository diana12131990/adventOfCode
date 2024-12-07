import re

f = open("day_4_input.txt","r")

letters = []
for line in f:
    line = line.strip()
    letters.append(line)
f.close()

direction = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
count = 0
rows = len(letters)
cols = len(letters[0])

for i in range(rows):
    for j in range(cols):
        for x,y in direction:
            if (letters[i][j] == "X" and 0 <= i+3*x < rows and 0 <= j+3*y < cols):
                search = "".join(letters[i+x*a][j+y*a] for a in range(4))
                if search == "XMAS":
                    count += 1
                    
print(count)