import re

f = open("day_13_input.txt","r")

button_a = []
button_b = []
prize = []
token = 0

for line in f:
    pos = re.findall(r'\d+',line)
    pos = [int(x) for x in pos]
    if "Button A" in line:
        button_a = pos.copy()
    elif "Button B" in line:
        button_b = pos.copy()
    elif "Prize" in line:
        prize = pos.copy()
        # A[0]x+B[0]y = prize[0]
        # A[1]x+B[1]y = prize[1]
        if (button_a[0] * button_b[1] - button_a[1] * button_b[0]) != 0:
            times_b = (button_a[0] * prize[1] - button_a[1] * prize[0]) / (button_a[0] * button_b[1] - button_a[1] * button_b[0])
            times_a = (prize[0] - button_b[0] * times_b) / button_a[0]
            if int(times_b) - times_b == 0 and int(times_a) - times_a == 0:
                token += int(times_a*3+times_b)
f.close()
print(token)