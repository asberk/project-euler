##############
## Problem 25
##
## What is the index of the first term in the Fibonacci sequence
## to contain 1000 digits?

def fib(n, lookup = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21}):
    if n not in lookup:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)
    return lookup[n]

n = 10

while n > 0:
    if len(str(fib(n)))==1000:
        print_sol(25, n)
        break
    
## 4782
