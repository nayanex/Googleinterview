#https://www.hackerrank.com/challenges/repeated-string/

"""
s = "a"
n = 1000000000000
"""

s = "a"
n =  882787

max_index = n - 1

repeated = 0

indexes = [i for i, elem in enumerate(s) if elem == 'a']

for occurrency in indexes:
    repeated += (max_index - occurrency)//len(s) + 1

print(repeated)
