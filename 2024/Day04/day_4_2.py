import re

f = open("day_4_input.txt","r")

letters = []
for line in f:
    line = line.strip()
    letters.append(line)
f.close()

count = 0
for i in range(1,len(letters)-1):
    for j in range(1,len(letters[0])-1):
        if (letters[i][j] == "A"):
            if ((letters[i-1][j-1] == "M" and letters[i+1][j+1] == "S") 
                or (letters[i-1][j-1] == "S" and letters[i+1][j+1] == "M")):
                if ((letters[i-1][j+1] == "M" and letters[i+1][j-1] == "S") 
                    or (letters[i-1][j+1] == "S" and letters[i+1][j-1] == "M")):
                    count += 1
                    
print(count)