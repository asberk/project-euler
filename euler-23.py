##############
## Problem 23
##

div_dict = { 1 : [], 2: [1], 3: [1], 4: [1,2], 5: [1], 6:[1,2,3],
             7: [1], 8:[1,2,4], 9:[1,3], 10:[1,2,5], 11:[1], 12:[1,2,3,4,6] }

## returns a list of the proper divisors of n
def proper_divisors(n, div_dict = { 1 : [], 2: [1], 3: [1], 4: [1,2], 5: [1], 6:[1,2,3] }):
    if n not in div_dict:
        dd = [1]
        j = 1
        cutoff = ceil(sqrt(n))+.5
        while j < cutoff:
            j+=1
            if j in dd:
                continue
            if n % j == 0:
                dd.append(j)
                dd.append(n/j)
                dd += proper_divisors(n/j, div_dict)
        div_dict[n] = sorted([e for i,e in enumerate(dd) if dd.index(e) == i ])
    return div_dict[n]
                    
## returns a list of the proper divisors of n
def divisors(n):
    dd = [1]
    j = 2
    cutoff = ceil(sqrt(n))+1
    while j < cutoff:
        if n % j == 0:
            dd.append(j)
            dd.append(n/j)
            # cutoff = n/j
        j+=1
    if len(dd)>1 and dd[-1] == dd[-2]:
        dd.remove(dd[-1])
    elif len(dd)>3 and dd[-1] == dd[-1-3] and dd[-1-1] == dd[-1-2]:
        dd.remove(dd[-1])
        dd.remove(dd[-2])
    return sorted(dd)

## computes the sum of the divisors of n    
def d(n):
    return sum(divisors(n))

## returns True if n is abundant
def is_abundant(n):
    if n < 12:
        return False
    return d(n)>n

# returns True if n is the sum of two abundant numbers
def is_abundant_sum(n):
    if n > 20161:
        return True
    for j in abundants_set:
        if j > n:
            return False
        if (n-j) in abundants_set:
            return True
    return False

N = 28123 # all numbers greater than this are abundant. 

print 'populating list of abundant numbers...'
abundant = [] ## sorted list of abundant numbers
n = 2
while n <= 28123:
    if is_abundant(n):
        abundant.append(n)
    n+=1

abundants_set = set(abundant)

print 'populating list of numbers that are not the sum of two abundant numbers...'
not_abundant_sum = [ x for x in range(1, 28123+1) if not is_abundant_sum(x) ]

print_sol(23, sum(not_abundant_sum)) ## 238500
