import re

f = open("day_22_input.txt","r")

def mix(number, value):
    return number ^ value

def prune(number):
    return number % 16777216

numbers = []
total = 0
for n in f:
    n = int(n.strip())
    for _ in range(2000):
        n = mix(n,n*64)
        n = prune(n)
        
        n = mix(n,n//32)
        n = prune(n)
        
        n = mix(n,n*2048)
        n = prune(n)
        
    total += n
f.close()

print(total)