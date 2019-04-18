n = 8
s = "UDDDUDUU"

sea_level = 0

valley_count = 0

mountain_or_valley = s[0]

for index, step in enumerate(s):
    if step == 'U':
        sea_level += 1
    else:
        sea_level -= 1
    if sea_level == 0:
        if mountain_or_valley == 'D':
            valley_count +=1
        if index < len(s) -1: 
            mountain_or_valley = s[index + 1]
        
print(valley_count)    


