import re

total_column = 50
total_row = 6

screen = []
for i in range(total_row):
    screen.append(["."]*total_column)


f = open("day_8_input.txt","r")

for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    if "rect" in line:
        column = int(numbers[0])
        row = int(numbers[1])
        for i in range(row):
            for j in range(column):
                if screen[i][j] == ".":
                    screen[i][j] = "#"
                else:
                    screen[i][j] = "."
    elif "row" in line:
        row = int(numbers[0])
        step = int(numbers[1])
        new_set = ["."]*total_column
        light_index = []
        for i in range(total_column):
            if screen[row][i] == "#":
                new_i = i + step
                if new_i >= total_column:
                    new_i -= total_column
                light_index.append(new_i)
        for i in light_index:
            new_set[i] = "#"
        for i in range(total_column):
            screen[row][i] = new_set[i]
        
    elif "column" in line:
        column = int(numbers[0])
        step = int(numbers[1])
        new_set = ["."]*total_row
        light_index = []
        for i in range(total_row):
            if screen[i][column] == "#":
                new_i = i + step
                if new_i >= total_row:
                    new_i -= total_row
                light_index.append(new_i)
        for i in light_index:
            new_set[i] = "#"
        for i in range(total_row):
            screen[i][column] = new_set[i]        
f.close()

for x in screen:
    print(x)