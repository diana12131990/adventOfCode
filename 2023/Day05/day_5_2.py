import re

f = open("day_5_input.txt","r")

source_data = {}
destination_data = {}


def Converter(c_map):
    # c_map[0] = destination range start, c_map[1] = source range start, c_map[2] = range length
    c_start = int(c_map[1])
    c_end = c_start + int(c_map[2])-1
    diff = int(c_map[0]) - c_start   
    
    # Detect in each source range, can ignore the new-split source data
    original_source_length = len(source_data)
    for i in range(original_source_length):
        s_start = source_data[i][0]
        s_end = source_data[i][1]
        
        # Get Overlap Range and assign to destination data
        i_range = range(max(c_start,s_start), min(c_end,s_end)+1)
        if (len(i_range)!=0):
            d_start = i_range[0] + diff
            d_end = i_range[-1] + diff
            destination_data.update({len(destination_data) : [d_start,d_end]})
            
            if s_start == i_range[0]:
                if s_end == i_range[-1]:                         #destination cover the whole range
                    source_data[i][0] = -1
                    source_data[i][1] = -1
                else:                                            #s_end > i_range[-1]
                    source_data[i][0] = i_range[-1]+1
            else:                                                #s_start < i_range[0]
                if s_end == i_range[-1]:                
                    source_data[i][1] = i_range[0]-1
                else:                                            #destination range covered by source range
                    new_s_end = source_data[i][1]
                    source_data[i][1] = i_range[0]-1
                    source_data.update({len(source_data) : [i_range[-1]+1 ,new_s_end]})

    
for line in f:
    line = line.strip()

    if re.search("seeds",line):
        s_info = re.findall('\d+',line)
        data_amount = len(s_info)/2
        
        for i in range(data_amount):
            x = i*2
            y = x+1
            
            s_start = int(s_info[x])
            s_end = s_start + int(s_info[y])-1
            
            source_data.update({i : [s_start,s_end]})
            
               
    elif re.search("map",line):
        
        # If we have converted data, transfer to source before running next map info
        if (len(destination_data)!=0): 
            for i in source_data:               # merge
                if source_data[i][0] != -1:
                    destination_data.update({len(destination_data) : source_data[i]})
            source_data = destination_data.copy()
            destination_data.clear()
            
        
    elif re.search(r'\d',line):
        convert_map = re.findall('\d+',line)
        Converter(convert_map)

# merge last time
for i in source_data:
    if source_data[i][0] != -1:
        destination_data.update({len(destination_data) : source_data[i]})


location = []
for i in destination_data:
    location.append(destination_data[i][0])
print(min(location))


f.close()