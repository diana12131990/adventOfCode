number = "01111001100111011"
disk_lengh = 35651584

while len(number) < disk_lengh:
    a = number
    b = a
    b = b[::-1]
    b = b.replace('0', '_').replace('1', '0').replace('_', '1')
    number = a + "0" + b
    
number = number[:disk_lengh]

Finish = False
while not Finish:
    checkrum = ""
    for i in range(len(number)/2):
        x = i*2
        y = i*2+1
        if number[x] == number[y]:
            checkrum += "1"
        else:
            checkrum += "0"
    number = checkrum
    if len(number)%2 != 0:
        Finish = True
print(number)