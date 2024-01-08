line = "1113222113"

for i in range(40):
    new_line = ""
    
    digit = "0"
    count = 0
    for x in line:
        if x != digit:            
            if digit != "0":
                new_line += str(count)+digit
            digit = x
            count = 1            
        else:
            count += 1
    new_line += str(count)+digit
    #print(new_line)
    line = new_line

print(len(line))