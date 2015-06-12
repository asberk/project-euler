##############
## Problem 17:
##
## If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
## If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
## words, how many letters would be used?
##
## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
##       forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
##       20 letters. The use of "and" when writing out numbers is in compliance 
##       with British usage.

## input an integer n between 1 and 1000 (inclusive) and output that number,
## printed according to British English (e.g., 1 -> one, 1000 -> one thousand)

dictionary = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
               11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 
               19:'nineteen', 0:'',
               20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 
               100:'onehundredand', 200:'twohundredand', 300:'threehundredand', 400:'fourhundredand', 500:'fivehundredand', 
               600: 'sixhundredand' , 700:'sevenhundredand', 800:'eighthundredand', 900:'ninehundredand', 1000:'onethousand' }
lengths = { key : len(value) for key,value in dictionary.items() }
def transcribe( n ):
    if n not in dictionary: 
        s = str(n)
        s = [ int(s[-1-j])*10**j for j in range(len(s))[::-1] ]
        if s[1] == 10:
            s = [s[0], s[1] + s[2]]
        dictionary[n] = ''.join([ dictionary[s[j]] for j in range(len(s)) ])
    return dictionary[n]

for j in range(1, 1001):
    transcribe(j)
    print j, dictionary[j]

for j in range(1,10):
    dictionary[j*100] = dictionary[j] + 'hundred'

lengths = {key : len(value) for key,value in dictionary.items() }

print_sol(17, sum(lengths.values())) ## 21124
