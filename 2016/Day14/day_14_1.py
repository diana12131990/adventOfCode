import hashlib

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

salt = "ahsbgdzn"
i = 0
keys_amount = 0
while keys_amount != 64:
    test_str = salt + str(i)
    code = hashlib.md5(test_str).hexdigest()
    Found,digit = FindTriple(code)
    if Found:
        for j in range(i+1,i+1001):
            test_str = salt + str(j)
            code = hashlib.md5(test_str).hexdigest()   
            if FindFixth(code,digit):
                keys_amount += 1
                break
    i += 1
i -= 1
print(i)