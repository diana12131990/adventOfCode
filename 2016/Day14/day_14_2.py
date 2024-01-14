import hashlib

salt = "ahsbgdzn"
hashes = []

def FindTriple(line):
    for i in range(1,len(line)-1):
        if line[i-1] == line[i] == line[i+1]:
            return True,line[i-1]
    return False,"None"

def FindFixth(line,digit):
    for i in range(2,len(line)-2):
        if digit == line[i-2] == line[i-1] == line[i] == line[i+1] == line[i+2]:
            return True
    return False            

def FindHash(index):
    if len(hashes) == index:
        test_str = salt + str(index)
        for x in range(2017):
            test_str = hashlib.md5(test_str).hexdigest()
        hashes.append(test_str)
        return test_str
    else:
        return hashes[index]
i = 0
keys_amount = 0
while keys_amount != 64:
    code = FindHash(i)
    Found,digit = FindTriple(code)
    if Found:
        for j in range(i+1,i+1001):
            code = FindHash(j)
            if FindFixth(code,digit):
                keys_amount += 1
                break
    i += 1
i -= 1
print(i)