#1! and 0! are 1. others are recursively calculated
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

#n is total, k is selection
def choose(n,k):
    top = factorial(n)
    bottom = factorial(k) * factorial(n-k)
    return top/bottom

#binomial event. success = prob, failure = 1-prob.
# class BinEvent:
    # def __init__(self, prob):
    #     self.prob = prob
    #     self.fail = 1-prob
#ddum = BinEvent(0.7)
#print(ddum.prob, ddum.fail)

#don't want to use this class for now. just p value is ok


#n = trials amount, k = exact amount of successes
def bernoulli(p, n, k):
    a = choose(n,k)
    b = p**k
    c = (1-p)**(n-k)
    return a*b*c

print(bernoulli(0.6,4,2)) #exactly 2 successes in 4 trials


#with only n, prints bernoulli for values k = 0 to n
def all_bernoulli(p, n):
    print("All bernoulli. Event p = ", p)
    print("n = ", n)
    for k in range (n+1): #k = 0, 1, ... n-1, n
        print(k, " --- ", bernoulli(p,n,k))
    print("-----")

all_bernoulli(0.6,6)


#prints bernoulli for values in between k and n.
def at_least(p, n, least):
    print("At least bernoulli. Event p = ", p, ", n = ", n)
    print("At least k = ", least)
    for k in range(least,(n+1)): #k = least, least+1, ... n-1, n
        print(k, " --- ", bernoulli(p,n,k))
    print("-----")

at_least(0.6,6,4)
