import math as m

def sumofFactors(n):

    result = 1
    for i in range(2, int(m.sqrt(n) + 1)):

        current_sum = 1
        current_term = 1

        while n % i == 0:
            n = n / i;
            current_term = current_term * i;
            current_sum += current_term;

        result = result * current_sum

    if n > 2:
        result = result * (1 + n)
        
    return result


threhold = 29000000
house = 1
while True:
    if (1+house)*house/2 >= threhold/10:
        present = sumofFactors(house)*10
        print(house, present)
        if present >= threhold:  
            break
    house += 1

print(house)