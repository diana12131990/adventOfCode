import hashlib

door_id = "cxdnnyjw"

i = 0
password = ["_","_","_","_","_","_","_","_"]
digit_count = 0
while digit_count < 8:
    test_str = door_id + str(i)
    code = hashlib.md5(test_str).hexdigest()
    if code[:5] == "00000":
        pos = code[5]
        digit = code[6]
        if pos.isdigit():
            pos = int(pos)
            if 0 <= pos <= 7:
                if password[pos] == "_":
                    password[pos] = code[6]
                    digit_count += 1
    i += 1

print("".join(password))