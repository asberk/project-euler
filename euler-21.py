##############
## Problem 21
##
## Find the sum of all amicable numbers under 10 000

## returns a list of the divisors of n
def divisors(n):
    dd = [1]
    j = 2
    cutoff = n
    while j < cutoff:
        if n % j == 0:
            dd.append(j)
            if not j==n/j: 
                dd.append(n/j)
            cutoff = n/j
        j+=1
    return sorted(dd)

## computes the sum of the divisors of n    
def d(n):
    return sum(divisors(n))


amicable = []
## 220 is the smallest amicable number
for n in range(220,10000):
    ## if we've already seen it, don't bother
    if n in amicable:
        continue
    ## compute the sum of the divisors
    dn = d(n)
    ## if the number is not perfect, but amicable
    if n == d(dn) and not n==dn:
        print n,d(n) # print the pair
        amicable.append(n) # append both to the list
        amicable.append(d(n))

## print the sum of all amicable numbers less than 10000
print_sol(21, sum(amicable)) ## 31626
    
