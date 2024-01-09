import re

f = open("day_2_input.txt","r")

digit = "5"
code = ""

def MoveDigit(d,x):
    if d == "5" and x == "R":
        return "6"
    
    elif d == "2":
        if x == "R":
            return "3"
        elif x== "D":
            return "6"
    elif d == "6":
        if x == "U":
            return "2"
        elif x == "R":
            return "7"
        elif x == "D":
            return "A"
        elif x == "L":
            return "5"
    elif d == "A":
        if x == "U":
            return "6"
        elif x == "R":
            return "B"
    
    elif d == "1" and x == "D":
        return "3"
    elif d== "3":
        if x == "U":
            return "1"
        elif x == "R":
            return "4"
        elif x == "D":
            return "7"
        elif x == "L":
            return "2"
    elif d== "7":
        if x == "U":
            return "3"
        elif x == "R":
            return "8"
        elif x == "D":
            return "B"
        elif x == "L":
            return "6" 
    elif d== "B":
        if x == "U":
            return "7"
        elif x == "R":
            return "C"
        elif x == "D":
            return "D"
        elif x == "L":
            return "A"
    elif d== "D" and x == "U":
        return "B"
        
    elif d== "4":
        if x == "D":
            return "8"
        elif x == "L":
            return "3"
    elif d== "8":
        if x == "U":
            return "4"
        elif x == "R":
            return "9"
        elif x == "D":
            return "C"
        elif x == "L":
            return "7"
    elif d== "C":
        if x == "U":
            return "8"
        elif x == "L":
            return "B"
    
    elif d == "9" and x == "L":
        return "8"
    
    return d

for line in f:
    line = line.strip()
    for x in line:
        digit = MoveDigit(digit,x)

    code += digit
f.close()

print(code)