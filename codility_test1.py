import operator

candies = [3, 4, 7, 7, 6, 6] 

n_give =  len(candies)//2

candy_freq = [candies.count(p) for p in candies]
dict_candies = (dict(zip(candies,candy_freq)))

while(n_give > 0):
    max_ele = max(dict_candies.items(), key=operator.itemgetter(1))[0]
    if(dict_candies[max_ele] == 1):
        n_give -= 1
        del dict_candies[max_ele]
    else:
        
        print(max_ele)
        subtract_from = dict_candies[max_ele]
        dict_candies[max_ele] -= subtract_from -1
        print(dict_candies)

        n_give -= subtract_from -1
        print(n_give)

    
print(len(dict_candies))