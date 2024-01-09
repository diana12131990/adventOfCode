import hashlib

door_id = "cxdnnyjw"
i = 0
password = ""
while len(password) != 8:
    test_str = door_id + str(i)
    code = hashlib.md5(test_str).hexdigest()
    if code[:5] == "00000":
        password += code[5]
    i += 1
print(password)