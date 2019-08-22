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

#with only n, prints bernoulli for values k = 0 to n
def all_bernoulli(p, n):
    result = [[],[]] #result[0] is x-axis, result[1] is y-axis.
    for k in range (n+1): #k = 0, 1, ... n-1, n
        result[0].append(k)
        result[1].append(bernoulli(p,n,k))
    return result

def print_all_bernoulli(p, n):
    print("All bernoulli. Event p = ", p)
    print("n = ", n)
    for k in range (n+1): #k = 0, 1, ... n-1, n
        print(k, " --- ", bernoulli(p,n,k))
    print("-----")


#prints bernoulli for values in between k and n.
def at_least(p, n, least):
    result = [[],[]]
    for k in range(least,(n+1)): #k = least, least+1, ... n-1, n
        result[0].append(k)
        result[1].append(bernoulli(p,n,k))
    return result

def print_at_least(p, n, least):
    print("At least bernoulli. Event p = ", p, ", n = ", n)
    print("At least k = ", least)
    for k in range(least,(n+1)): #k = least, least+1, ... n-1, n
        print(k, " --- ", bernoulli(p,n,k))
    print("-----")

#Gonna try to use this as a module. First, put all the calls in here:
if __name__ == "__main__":
    print("Basic bernoulli: ",bernoulli(0.6,4,2))
    # print(all_bernoulli(0.6,6))
    # print_all_bernoulli(0.6,6)
    # print(at_least(0.6,6,4))
    # print_at_least(0.6,6,4)
##so that these don't happen on import. only when ran as script.
