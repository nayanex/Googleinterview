
candies = ["ba", "ba", "na", "aya", "aya"]
most_voted = []

votefreq = [candies.count(p) for p in candies]

dictcandies = (dict(zip(candies,votefreq)))

max_ele = max(zip(dictcandies.values(), dictcandies.keys()))

print(max_ele)

for name, vote in dictcandies.items():
    if vote == max_ele[0]:
        most_voted.append(name)


most_voted.sort()

last = len(most_voted) -1

print(most_voted[last])