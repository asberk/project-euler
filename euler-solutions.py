from math import * 
import copy
import operator

def print_sol(n, ans):
    print 'Problem ' + str(n) + ':'
    print ans
    print ''

## Problem 1:
## If we list all the natural numbers below 10 that are multiples
## of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
## 23. 
## Find the sum of all the multiples of 3 or 5 below 1000.
p1 = sum([ x for x in range(1000) if x % 3 == 0 or x % 5 == 0 ])
print_sol(1, p1)

## Problem 2:
## By considering the terms in the Fibonacci sequence whose values
## do not exceed four million, find the sum of the even-valued
## terms. 

def fib_le(n): 
    fib = [1, 1]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib

p2 = sum( [ x for x in fib_le(4e6) if x % 2 == 0 ] )
print_sol(2, p2)

#############
## Problem 3:
## What is the largest prime factor of the number 600851475143?
# need only to find primes less than sqrt(600851475143)
N = 600851475143.
n = floor(sqrt(N))

########
## Step 1: start with initial primes list
primes_list = [ 2., 3., 5., 7., 11., 13., 17., 19., 23., 29., 31. ]

########
## Step 2: functions for divisibility and testing primality

## returns True if N is prime
def is_prime(N, primes_list):
    N = float(N)
    if N <= primes_list[-1]**2 and N not in [0,1]:
        return not any( [ N/x == floor(N/x) for x in primes_list if x <= sqrt(N) ] )
    else:
        return False

## reduce number N by dividing it by any prime factors in primes_list
## returns the reduced N, and the largest prime x by which N was divisible (defaults to 1)
def div(N, primes_list, x=1.):
    ## keep only those primes that divide N 
    primes_list = filter( lambda y: N % y == 0, primes_list )
    ## if the list is non-empty...
    if any( primes_list ):
        ## set x to be the largest of dividing primes
        if x == 1. : x = max(primes_list)

        # reduce N by the first prime in the list
        # and recursively call the function on the new N
        N = float(N)/primes_list[0]
        return div(N, primes_list, x)
    else:
        ## return the reduced N and the largest dividing prime 
        ## of the input sequence (defaults to 1)
        return N, x

## Examples of div: 
## print div(N, primes_list)     # (  N,  1.0)
## print div(100, primes_list)   # (1.0,  5.0)
## print div(31**2, primes_list) # (1.0, 31.0)

#######
## Step 3: combine the above

## returns greatest prime factor of N
def GPF(N, primes_list):
    ## reduce N if possible, by dividing it by prime factors in primes_list (if there are any)
    N, xx = div(N, primes_list)
    ## if div reduced N to 1, then it returns the greatest prime factor; we're done! 
    if N == 1:
        return xx
    ## otherwise, compute (theoretical) max number of iterations we'll have to perform:
    n = sqrt(N)

    ## set j to be the next highest number after primes_list[-1], 
    ## and keep chugging!
    j = primes_list[-1] + 1 
    while j <= N: 
        ## add j to primes_list if j is prime
        ## and try to divide N by j
        if is_prime(j, primes_list):
            primes_list.append(j)
            N, junk = div(N,[j])
            ## sanity check for large number of iterations
            if len(primes_list)%1000 == 0 : print str(len(primes_list)) + ' iterations and counting...'
        j+=1 # update j

        ## j should never be greater than n; 
        ## largest number you have to check is less than or equal 
        ## to the square root of the original number
        if j > n: 
            raise ValueError('something went wrong; this many iterations shouldn\'t be needed')

    ## end of while loop; return the greatest prime number that divides N!
    return primes_list[-1]

###########
## Quadratic Sieve

## Let n be the number to be factored
n = 600851475143.

def Q(x, n):
    return (x + floor(sqrt(n)))**2 - n


#######
## Step 4: compute and print solution
p3 = GPF(N, primes_list)
## p3 = 6857.0
print_sol(3, p3)


#############
## Problem 4:
## Find the largest palindrome made from the product of two 3-digit numbers.
do_p4 = False

def is_palindrome(n):
    sn = str(n)
    max_l_idx = int(floor(.5*len(sn)))
    parity = [ sn[j] == sn[-1-j] for j in range(max_l_idx) ]
    return all(parity)


## Brute force approach
def brute_force_palindrome(n1, n2):
    biggest = [1, 1, 1]
    for j in range(n1)[::-1]:
        for k in range(j, n2)[::-1]:
            if is_palindrome(j*k) and j*k > biggest[0]:
                biggest = [j*k, j, k]
    return biggest

if do_p4:
    p4 = brute_force_palindrome(1000, 1000)
else:
    p4 = [906609, 913, 993]
print_sol(4, p4)

#############
## Problem 5:
## What is the smallest positive number that is evenly divisible by all 
## of the numbers from 1 to 20?

## i.e. find least common multiple of Prod(1, 20)
def gcd(a,b):
    if a < b:
        return gcd(b,a)
    tmp = divmod(a,b)
    if tmp[1] == 0:
        return b
    else: 
        return gcd(b,tmp[1])
    
## Vector GCD:
## ll is a list
def vector_gcd(ll):
    vgcd = {}
    for j in range(0,len(ll)-1):
        for k in range(j+1, len(ll)): # above triangle
            vgcd[(ll[k],ll[j])] = gcd(ll[k], ll[j])
    return vgcd

## for each prime less than 20, just count the largest number of factors that can fit below 20 
## (e.g., 2**4 = 16 < 20, 3**2 = 9 < 20 but 3**3 = 27 > 20)
lcm = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print_sol(5, lcm)

#############
## Problem 6: 
## Find the difference between the sum of the squares of the first 
## one hundred natural numbers and the square of the sum.

sumsq = reduce(lambda x,y: x+y, [ x**2 for x in range(1, 101) ])
sqsum = reduce(lambda x,y: x+y, range(1,101))**2

p6 = sqsum - sumsq
print_sol(6,p6)

## 
## Problem 7: 
## Find the 10001st prime number
do_p7 = False

if do_p7:
    j = primes_list[-1] + 1 
    while len(primes_list)<=10000: 
        ## add j to primes_list if j is prime
        ## and try to divide N by j
        if is_prime(j, primes_list):
            primes_list.append(j)
            ## sanity check for large number of iterations
            if len(primes_list)%1000 == 0 : 
                print str(len(primes_list)) + ' iterations and counting...'
        j+=1 # update j
    p7 = primes_list[10000]
else:
    p7 = 104743
print_sol(7,p7)

###
## Problem 8:
## Find the thirteen adjacent digits in the 1000-digit number 
## that have the greatest product. What is the value of this product?

n = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'

def prod_13(n, j):
    ## n is a string
    ## j is an index in (0, len(n)-1)
    return reduce(lambda x,y: int(x)*int(y), n[j:j+13])

biggest = 0
for j in range(1, len(n)-12):
    tmp = prod_13(n,j)

    if tmp > biggest:
        biggest = tmp
    if tmp == 0:
        j += 13

print_sol(8, biggest)


#############
## Problem 9:
## There exists exactly one Pythagorean triplet for which a + b + c = 1000. 
## Find the product abc.


## a^2 + b^2 = c^2


for a in range(1, 999):
    for b in range(1,999):
        c = 1000 - a - b
        if not c == sqrt(a**2 + b**2):
            continue
        else:
            print a,b,c
            abc = a*b*c
            break

print_sol(9, abc)


################
## Problem 10:
## Find the sum of all the primes below two million
do_p10 = True

if do_p10:
    N = 2e6
    pl = range(2, int(N))
    j = 0
    p = 2
    while p**2 <= N:
        pl = filter(lambda x: x % p != 0 or x == p, pl)
        j += 1
        p = pl[j]

    p10 = reduce(lambda x,y : x+y, pl) ## = 142913828922

else:
    p10 = 142913828922


print_sol(10,p10)



### Problem 11 is stupid

##############
## Problem 12: 
## 

## computes nth triangular number
def triangle(n):
    if n==1:
        return 1
    else:
        return n + triangle(n-1)

## Brute force one
def num_factors(n):
    nf = 0
    j = 1
    cutoff = n
    while j <= cutoff:
        if n % j == 0:
            nf += 1
        j+=1
    return nf

## smarter algorithm
## computes number of factors dividing n 
def num_factors(n):
    if n in [0,1]:
        return 1
    nf = 2 ## 1 and n
    j = 2 ## start by checking div by 2
    cutoff = floor(n/2) ## don't need to check past n/2
    while j <= cutoff:
        if n % j == 0 :
            if j**2 == n:
                nf+=1
            else:
                nf += 2
            cutoff = n/j-1
        j+=1
    return nf
j = 1
T = 1

while num_factors(T) < 500:
    j += 1
    T += j
print_sol(12, T) # 76576500


### Problem 13: Work out the first ten digits of the sum of the 
##              following one-hundred 50-digit numbers.
n_list = [37107287533902102798797998220837590246510135740250, 
46376937677490009712648124896970078050417018260538,
74324986199524741059474233309513058123726617309629,
91942213363574161572522430563301811072406154908250,
23067588207539346171171980310421047513778063246676,
89261670696623633820136378418383684178734361726757,
28112879812849979408065481931592621691275889832738,
44274228917432520321923589422876796487670272189318,
47451445736001306439091167216856844588711603153276,
70386486105843025439939619828917593665686757934951,
62176457141856560629502157223196586755079324193331,
64906352462741904929101432445813822663347944758178,
92575867718337217661963751590579239728245598838407,
58203565325359399008402633568948830189458628227828,
80181199384826282014278194139940567587151170094390,
35398664372827112653829987240784473053190104293586,
86515506006295864861532075273371959191420517255829,
71693888707715466499115593487603532921714970056938,
54370070576826684624621495650076471787294438377604,
53282654108756828443191190634694037855217779295145,
36123272525000296071075082563815656710885258350721,
45876576172410976447339110607218265236877223636045,
17423706905851860660448207621209813287860733969412,
81142660418086830619328460811191061556940512689692,
51934325451728388641918047049293215058642563049483,
62467221648435076201727918039944693004732956340691,
15732444386908125794514089057706229429197107928209,
55037687525678773091862540744969844508330393682126,
18336384825330154686196124348767681297534375946515,
80386287592878490201521685554828717201219257766954,
78182833757993103614740356856449095527097864797581,
16726320100436897842553539920931837441497806860984,
48403098129077791799088218795327364475675590848030,
87086987551392711854517078544161852424320693150332,
59959406895756536782107074926966537676326235447210,
69793950679652694742597709739166693763042633987085,
41052684708299085211399427365734116182760315001271,
65378607361501080857009149939512557028198746004375,
35829035317434717326932123578154982629742552737307,
94953759765105305946966067683156574377167401875275,
88902802571733229619176668713819931811048770190271,
25267680276078003013678680992525463401061632866526,
36270218540497705585629946580636237993140746255962,
24074486908231174977792365466257246923322810917141,
91430288197103288597806669760892938638285025333403,
34413065578016127815921815005561868836468420090470,
23053081172816430487623791969842487255036638784583,
11487696932154902810424020138335124462181441773470,
63783299490636259666498587618221225225512486764533,
67720186971698544312419572409913959008952310058822,
95548255300263520781532296796249481641953868218774,
76085327132285723110424803456124867697064507995236,
37774242535411291684276865538926205024910326572967,
23701913275725675285653248258265463092207058596522,
29798860272258331913126375147341994889534765745501,
18495701454879288984856827726077713721403798879715,
38298203783031473527721580348144513491373226651381,
34829543829199918180278916522431027392251122869539,
40957953066405232632538044100059654939159879593635,
29746152185502371307642255121183693803580388584903,
41698116222072977186158236678424689157993532961922,
62467957194401269043877107275048102390895523597457,
23189706772547915061505504953922979530901129967519,
86188088225875314529584099251203829009407770775672,
11306739708304724483816533873502340845647058077308,
82959174767140363198008187129011875491310547126581,
97623331044818386269515456334926366572897563400500,
42846280183517070527831839425882145521227251250327,
55121603546981200581762165212827652751691296897789,
32238195734329339946437501907836945765883352399886,
75506164965184775180738168837861091527357929701337,
62177842752192623401942399639168044983993173312731,
32924185707147349566916674687634660915035914677504,
99518671430235219628894890102423325116913619626622,
73267460800591547471830798392868535206946944540724,
76841822524674417161514036427982273348055556214818,
97142617910342598647204516893989422179826088076852,
87783646182799346313767754307809363333018982642090,
10848802521674670883215120185883543223812876952786,
71329612474782464538636993009049310363619763878039,
62184073572399794223406235393808339651327408011116,
66627891981488087797941876876144230030984490851411,
60661826293682836764744779239180335110989069790714,
85786944089552990653640447425576083659976645795096,
66024396409905389607120198219976047599490197230297,
64913982680032973156037120041377903785566085089252,
16730939319872750275468906903707539413042652315011,
94809377245048795150954100921645863754710598436791,
78639167021187492431995700641917969777599028300699,
15368713711936614952811305876380278410754449733078,
40789923115535562561142322423255033685442488917353,
44889911501440648020369068063960672322193204149535,
41503128880339536053299340368006977710650566631954,
81234880673210146739058568557934581403627822703280,
82616570773948327592232845941706525094512325230608,
22918802058777319719839450180888072429661980811197,
77158542502016545090413245809786882778948721859617,
72107838435069186155435662884062257473692284509516,
20849603980134001723930671666823555245252804609722,
53503534226472524250874054075591789781264330331690]


p13 = str(reduce(lambda x,y: x + y, n_list))[:10]

print_sol(13, p13)


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

while n < 1e6:
    n += 1
    if n in lengths:
        continue
    collatz_length(n, lengths)

best = max(lengths.iteritems(), key = operator.itemgetter(1))[0]
print_sol(14, best) ## 837799.0



##############
## Problem 15:
## 

def traverse( node, node_dict={(0,0) : 0, (1,0): 1, (0,1): 1, (1,1): 2 } ):
    if node not in node_dict:
        nbr_u = ( node[0]-1, node[1] )
        nbr_l = ( node[0], node[1]-1 )
        if -1 in nbr_u: 
            node_dict[node] = traverse(nbr_l, node_dict)
        elif -1 in nbr_l:
            node_dict[node] = traverse(nbr_u, node_dict)
        else:
            node_dict[node] = traverse(nbr_u, node_dict) + traverse(nbr_l, node_dict)
    return node_dict[node]

print traverse( (20,20) ) ## 137846528820

###############
## Problem 16:
##
## 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
## What is the sum of the digits of the number 2**1000?

n = str(2**1000)
n2 = [ int(n[j]) for j in range(len(n)) ]
print_sol(16, sum(n2)) ## 1366


