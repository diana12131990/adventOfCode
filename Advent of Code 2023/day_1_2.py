import re

f = open("day_1_input.txt","r")
word_list = ["one","two","three","four","five","six","seven","eight","nine"]
sum = 0


for line in f:
    
    # Find the first and last digit index first
    digit_index = re.search(r'\d',line)
    if digit_index:
        first_index = digit_index.start()
        reverse_line = line[::-1]
        digit_index = re.search(r'\d',reverse_line)
        last_index = (len(line)-1) - digit_index.start()
    else:
        first_index = 9999
        last_index = -1

    # Find the first and last digit
    digits = re.findall(r'\d',line)
    if digits:
        first = digits[0]
        last = digits[-1]
        
    # Detect number word in the line and get their index, if indext is smaller than first or bigger than last, switch to new number
    for num_word in word_list:
        if num_word in line:
            num = word_list.index(num_word) + 1
            pos_idx=[]
            word_count = line.count(num_word)
            pos = line.find(num_word)
            pos_idx.append(pos)
            word_count -= 1
            while word_count >= 1:
                old_pos = pos+1
                pos = line[old_pos:].find(num_word) + old_pos
                pos_idx.append(pos)
                word_count -= 1 
            if pos_idx[0] < first_index:
                first_index = pos_idx[0]
                first = num
            if pos_idx[-1] > last_index:
                last_index = pos_idx[-1]
                last = num
                
    num = int(str(first)+str(last))
    sum += num


print(sum)
f.close()