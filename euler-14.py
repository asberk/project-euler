import operator

##############
## Problem 14:
## 

def collatz_length(n, lengths = {1 : 1, 2: 2}):
    if n not in lengths:
        if n % 2 == 0:
            m = .5*n
        else: 
            m = 3*n + 1
        lengths[n] = 1 + collatz_length(m, lengths)
    return lengths[n]

n = 0.
lengths = { 1: 1, 2: 2, 3: 8, 4: 3 }
seen = [n]

while n < 1e6:
    n += 1
    if n in lengths:
        continue
    collatz_length(n, lengths)

best = max(lengths.iteritems(), key = operator.itemgetter(1))[0]
print best ## 837799.0

