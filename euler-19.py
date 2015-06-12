##############
## Problem 19:
##
## You are given the following information, but you may prefer to do some research for yourself.
##
## 1 Jan 1900 was a Monday.
## Thirty days has September,
## April, June and November.
## All the rest have thirty-one,
## Saving February alone,
## Which has twenty-eight, rain or shine.
## And on leap years, twenty-nine.
## A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
## How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

##                      Sun, Mon, ..., Sat
## vector; elements in {  0,   1, ...,   6}
weekdays = range(2, 7)
years = range(1901, 2001)
months = range(12) ## 0 = January, 1 = February, ...
days = []

for y in years:
    for m in months:
        if m in [8,3,5,10]: # september, april, june, november
            days += range(30)
        elif m in [0, 2, 4, 6, 7, 9, 11]:
            days += range(31)
        else: # m = 1 = February
            if y % 4 == 0:
                days += range(29)
            else:
                days += range(28)

weekdays += range(7)*int(ceil(float(len(days))/7))
first_suns = [1 for j in range(len(days)) if days[j] == 0 and weekdays[j] == 0 ]
print_sol(19, sum(first_suns)) ## 171
