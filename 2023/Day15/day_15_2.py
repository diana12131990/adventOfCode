import re

f = open("day_15_input.txt","r")
line = f.readline()
f.close()

def getASCII(tag):
     current_value = 0
     for x in tag:
          # change to ASCII code and add to current value
          current_value += ord(x)
          # multiply 17
          current_value *= 17
          # get remainder from division by 256
          current_value %= 256
     return current_value

total_value = 0
box = {}

while line != "":
     find_comma = re.search(",",line)
     if find_comma:
          comma_index = find_comma.start()
          check_string = line[:comma_index]
          line = line[comma_index+1:]
     else:
          check_string = line
          line = ""
     
     
     if "=" in check_string:
          tag, value = check_string.split("=")
          key = getASCII(tag)
          if not box.has_key(key):
               box.update({key:[]})
               
          hasValue = False
          for array in box[key]:
               if array[0] == tag:
                    array[1] = value
                    hasValue = True
                    break
          if not hasValue:
               box[key].append([tag,value])
                    
          
     elif "-" in check_string:
          tag = check_string[:-1]
          key = getASCII(tag)
          if box.has_key(key):
               for array in box[key]:
                    if array[0] == tag:
                         box[key].remove(array)
                         if box[key] == []:
                              box.pop(key)
                         break
print(box)

total_value = 0
for key in box:
     for i in range(len(box[key])):
          total_value += (key+1) * (i+1) * int(box[key][i][1])
print(total_value)