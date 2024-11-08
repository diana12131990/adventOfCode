import re

value_a = 679
value_b = 771

factor_a = 16807
factor_b = 48271

divisor = 2147483647

def get_new_value(old_value,factor):
    return old_value * factor % divisor

def compare_two_value(a,b):
    binary_a = bin(a)[2:].zfill(32)
    binary_b = bin(b)[2:].zfill(32)
    if binary_a[-16:] == binary_b[-16:]:
        return True
    else:
        return False


judge = 0
for i in range(5000000):
    value_a = get_new_value(value_a,factor_a)
    while value_a%4 != 0:
        value_a = get_new_value(value_a,factor_a)
    
    value_b = get_new_value(value_b,factor_b)
    while value_b%8 != 0:
        value_b = get_new_value(value_b,factor_b)

    if compare_two_value(value_a,value_b):
        judge += 1

print(judge)