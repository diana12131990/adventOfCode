import re

f = open("day_5_input.txt","r")

garden = {
    "seed":       [],
    "soil":       [],
    "fertilizer": [],
    "water":      [],
    "light":      [],
    "temperature":[],
    "humidity":   [],
    "location":   []
}

def Converter(source, destination, c_map):
    # c_map[0] = destination range start, c_map[1] = source range start, c_map[2] = range length
    s_info = garden[source]
    s_start = int(c_map[1])
    s_end = s_start + int(c_map[2])-1
    diff = int(c_map[0]) - s_start
    
    for i in range(len(s_info)):
        if s_start <= s_info[i] <= s_end:
            garden[destination][i] = s_info[i] + diff
    
    
for line in f:
    line = line.strip()
    
    if re.search("seeds",line):
        garden["seed"] = re.findall('\d+',line)
        seed_amount = len(garden["seed"])
        for i in range(seed_amount):
            garden["seed"][i] = int(garden["seed"][i])
        
    elif re.search("map",line):
        line = line.replace(" map:","")
        source,destination = re.split("-to-",line)
        for i in range(seed_amount):        
            garden[destination].append(garden[source][i])
        
    elif re.search(r'\d',line):
        convert_map = re.findall('\d+',line)
        Converter(source, destination, convert_map)
        

print(min(garden["location"]))
f.close()