
import re

f = open("day_5_input.txt","r")

fresh_ranges_original = []
for line in f:
    line = line.strip()
    if line == "":
        break
        
    start, end = line.split('-')
    fresh_ranges_original.append([int(start),int(end)])

f.close()

# sorting it first can help us know the start number is already in order when merging,
# and we just need to check the end number from the merge ranges
fresh_ranges_original.sort(key=lambda x:[x[0],x[1]])

fresh_ranges_merged = []
for start, end in fresh_ranges_original:
    
    # if nothing in the merge list
    # or start number is at least 2 bigger than the last range's end number (like [5,8] and [1,3])
    # add this range into the merge as the new one. 
    # And because we already do the sorting, we already know this new range will have bigger start then the existed one
    if not fresh_ranges_merged or start > fresh_ranges_merged[-1][1] + 1:
        fresh_ranges_merged.append([start,end])
    
    # if the start number is in the range of the last range (like [5,8] and [1,4] or [5,8] and [1,9])
    # merge it by checking the which number is bigger, the range's end number or the end in current
    # i.e [5,8] merge to [1,4] will be [1,8], and [5,8] merge to [1,9] will still be [1,9] because 9 > 8
    # And again, because we sorted before, 
    # we know the all the existed merge ranges before the last will be smaller than current range
    else:
        fresh_ranges_merged[-1][1] = max(fresh_ranges_merged[-1][1],end)


total_fresh = 0
for start, end in fresh_ranges_merged:
    total_fresh += (end - start + 1)

print(total_fresh)
