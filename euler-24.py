##############
## Problem 24:
##
## A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation 
## of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, 
## we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
##
## 012   021   102   120   201   210
##
## What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


def perm(n):
    if len(n) == 1:
        return [n]
    else: 
        perms = []

        for j in range(len(n)):
            tmp = perm(n[0:j] + n[j+1:])
            for k in range(len(tmp)):
                perms.append([n[j]]+tmp[k])
        return perms


ten_perms = sorted(perm([0,1,2,3,4,5,6,7,8,9]))
millionth = ten_perms[999999] ## [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]

