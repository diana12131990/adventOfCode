import re

def RunResult(data,rule):
    if rule == "A":
        return True
    elif rule == "R":
        return False
    else:
        return RunRule(data,rule)    
    

def RunRule(data,name):
    rules = rules_dic[name]
    i = 0
    while i < len(rules):
        s_rule = rules[i]
        if re.search(":",s_rule):
            compare, result = re.split(":",s_rule)
            #print(compare,result)
            if compare[1] == "<" and data[compare[0]] < int(compare[2:]):
                return RunResult(data,result)
            elif compare[1] == ">" and data[compare[0]] > int(compare[2:]):
                return RunResult(data,result)
            else:
                i += 1
        else:
            #print(s_rule)
            return RunResult(data,s_rule)

f = open("day_19_input.txt","r")

rules_dic = {}
total_value = 0

for line in f:
    line = line.strip()
    
    if line != "":
        if line[0] != "{":
            name, rules_string = re.split("{",line)
            rules_string = rules_string.replace("}","")
            rules = re.split(",",rules_string)
            rules_dic.update({name:rules})
            
        else:
            line = line.replace("{","")
            line = line.replace("}","")
            line = re.split(",",line)
            data = {}
            for x in line:
                category, number = re.split("=",x)
                data.update({category:int(number)})
            if RunRule(data, "in"):
                total_value += sum(data.values())
            data.clear()
f.close()

print(total_value)