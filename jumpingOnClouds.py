cloud_array0 = [0, 1, 0, 0, 0, 1, 0] #3
cloud_array1 = [0, 0, 1, 0, 0, 1, 0] # 4
cloud_array2 = [0, 0, 0, 0, 1, 0] #3
cloud_array3 = [0, 0, 0, 1, 0, 0] #3

min_jumps = 0
n = len(cloud_array3)

start_jump = cloud_array3[0]
current_jump = 0

while(current_jump <= n - 2):
    print(current_jump)
    if (n - current_jump) >= 3 and cloud_array3[current_jump + 2] == 0:
        current_jump = current_jump + 2

    else:
        current_jump = current_jump + 1
    min_jumps += 1

print(min_jumps)

