import re

f = open("day_15_input.txt","r")
line = f.readline()
f.close()

total_value = 0
while line != "":
     find_comma = re.search(",",line)
     if find_comma:
          comma_index = find_comma.start()
          check_string = line[:comma_index]
          line = line[comma_index+1:]
     else:
          check_string = line
          line = ""
     
     current_value = 0
     for x in check_string:
          # change to ASCII code and add to current value
          current_value += ord(x)
          # multiply 17
          current_value *= 17
          # get remainder from division by 256
          current_value %= 256
     total_value += current_value
     
print(total_value)


    