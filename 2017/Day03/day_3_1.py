
input_num = 277678
step = 0

sqrt_num = int(input_num**0.5)
time_number = sqrt_num * sqrt_num

remain = input_num - time_number

if remain == 0:
    step = sqrt_num - 1

elif remain < sqrt_num/2:
    step += sqrt_num/2 - remain
    step += sqrt_num/2
    if sqrt_num%2 == 1:
        step += 1
elif remain <= sqrt_num:
    step += remain - sqrt_num/2 - 1
    step += sqrt_num/2
    if sqrt_num%2 == 1:
        step += 1

else:
    step += sqrt_num/2
    if sqrt_num%2 == 1:
        step += 1
        
    remain -= sqrt_num
    if remain < sqrt_num/2:
        step += sqrt_num/2 - remain  
    else:
        step += remain - sqrt_num/2 - 1
    
    
print(step)