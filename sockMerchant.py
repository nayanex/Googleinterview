def sockMerchant(n, ar):
    pairs = 0
    ar.sort()
    ar.append('-1')
    i = 0
    while i<n:ar.append('-1')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            pairs = pairs+1
            i+=2
        else:
            i+=1
        if ar[i]==ar[i+1]:
            pairs = pairs+1
            i+=2
        else:
            i+=1
    return pairs