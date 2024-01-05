import hashlib

input_str = "ckczppom"
i = 0
while True:
    test_str = input_str + str(i)
    code = hashlib.md5(test_str).hexdigest()
    if code[:5] == "00000":
        break
    else:
        i += 1
        
print(i)