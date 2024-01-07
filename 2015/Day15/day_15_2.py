import re

f = open("day_15_input.txt","r")

ingredients = []
for line in f:
    line = line.strip()
    numbers = re.findall("-?\d+",line)
    numbers = [int(x) for x in numbers]
    ingredients.append(numbers)
        
f.close()

total_spoon = 100
max_score = 0
for a in range(1,total_spoon-len(ingredients)+2):
    for b in range(1,total_spoon - a - len(ingredients)+2 - 1):
        for c in range(1,total_spoon - a - b - len(ingredients)+2 - 2):
            skip = False
            d = total_spoon - a - b - c
            
            current_score = 1
            for i in range(4):
                score = ingredients[0][i]*a+ingredients[1][i]*b+ingredients[2][i]*c+ingredients[3][i]*d
                if score <= 0:
                    skip = True
                    break
                else:
                    current_score *= score
            if not skip and current_score > max_score:
                if ingredients[0][4]*a+ingredients[1][4]*b+ingredients[2][4]*c+ingredients[3][4]*d == 500:
                    max_score = current_score
print(max_score)