import re
from itertools import groupby

password = [x for x in "hxbxxyzz"]

def HasContinueChar(line):
    for i in range(1,len(line)-1):
        if ord(line[i-1]) + 1 == ord(line[i]) and ord(line[i]) == ord(line[i+1]) - 1:
            return True
    return False
        
def NoIOL(line):
    if "i" in line or "o" in line or "l" in line:
        return False
    return True

def HasDoubleDoubleChar(line):
    same_char_group = [len(list(j)) for _, j in groupby(line)]
    count = 0
    for x in same_char_group:
        if x > 1:
            count += 1
            if count == 2:
                return True
    return False

while True:
    Found = False
    for i in reversed(range(len(password))):
        ch = password[i]
        if ch != "z":
            password[i] = chr(ord(ch) + 1)
            Found = True
            break
        else:
            password[i] = "a"
    if not Found:
        password.insert(0,"a")
    new_password = "".join(password)
        
    
    if HasContinueChar(new_password) and NoIOL(new_password) and HasDoubleDoubleChar(new_password):
        print(new_password)
        break