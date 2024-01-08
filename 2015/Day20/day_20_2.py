import math  

def divSum(n) :
    if n == 1:
        return 1

    result = n
    if n <= 50:
        result += 1    
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i == 0 :
            j = n/i
            
            if j<=50:
                result += i  
            if j != i and i <= 50:
                result += j
    return result

house = 1
threhold = 29000000

while True:
    if ((house-49)+house)*50/2 >= threhold/11:
        present = divSum(house)*11
        print(house, present)
        if present >= threhold:  
            break
    house += 1

print(house)