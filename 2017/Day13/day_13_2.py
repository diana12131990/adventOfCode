import re
f = open("day_13_input.txt","r")

firewall = {}
for line in f:
    line = line.strip()
    numbers = re.findall(r"\d+",line)
    firewall.update({int(numbers[0]):int(numbers[1])})
f.close()

delay = 0
while any(((depth + delay) % (2 * (rng - 1)) == 0) for depth, rng in firewall.items()):
    delay += 1
        
print(delay)