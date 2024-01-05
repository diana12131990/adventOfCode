import re
from itertools import groupby

f = open("day_5_input.txt","r")

vowels = ["a","e","i","o","u"]
naughty_str = ["ab","cd","pq","xy"]

def HasEnoughVowel(line):
    count = 0
    for x in line:
        if x in vowels:
            count += 1
            if count >= 3:
                return True
    return False

def HasDoubleChar(line):
    same_char_group = [len(list(j)) for _, j in groupby(line)]
    for x in same_char_group:
        if x > 1:
            return True
    return False

def NoNaughtyStr(line):
    for x in naughty_str:
        if x in line:
            return False
    return True

nice = 0
for line in f:
    line = line.strip()
    if HasEnoughVowel(line) and HasDoubleChar(line) and NoNaughtyStr(line):
        nice += 1
        
f.close()

print(nice)