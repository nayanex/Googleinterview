# https://www.hackerrank.com/challenges/equality-in-a-array/problem

from collections import Counter

arr = [3, 3, 2, 1, 3, 3]
min_elem_to_del = 0

dict_elem = Counter(arr)

most_freq_key = dict_elem.most_common(1)[0][0]

del dict_elem[most_freq_key]

for elem in dict_elem.values():
    min_elem_to_del += elem


print(min_elem_to_del)



"""

for key, value in dict_elem.items():
    print(str(key) + ", " + str(value))


dict_elem.most_common(1)[0][0]

for item in arr:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict = 1
"""
