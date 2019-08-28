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


def all_bernoulli(p, n, printing=False):
    if printing:
        print("All bernoulli. Event p = ", p)
        print("n = ", n)
    else:
        result = [[],[]]
    for k in range (n+1): #k = 0, 1, ... n-1, n
        berntemp = bernoulli(p,n,k)
        if printing:
            print(k, " --- ", berntemp)
        else:
            result[0].append(k)
            result[1].append(berntemp)
    if printing:
        print("-----")
    else:
        return result

#prints bernoulli for values in between k and n.
def at_least(p, n, least, printing=False):
#Check if it can actually be done. least cant be bigger
    if (least <= n):
        sum = 0
        if printing:
            print("At least bernoulli. Event p =", p, ", n =", n)
            print("At least k =", least)
            print("Probabilities of k, k+1, k+2, ... n-1, n are:")
        else:
            result = [[],[],sum]
        for k in range(least,(n+1)): #k = least, least+1, ... n-1, n
            berntemp = bernoulli(p,n,k)
            if printing:
                print(k, " --- ", berntemp)
            else:
                result[0].append(k)
                result[1].append(berntemp)
            sum = sum + berntemp
        if printing:
            print("")
            print("Probability of at least " + str(least) + " successes is the sum: " + str(sum))
            print("-----")
        else:
            result[2] = sum
            return result
    else:
        return "Least " + str(least) + " must be smaller than n " + str(n) +"."


#Gonna try to use this as a module. First, put all the calls in here:
if __name__ == "__main__":
    # print("Basic bernoulli: ",bernoulli(0.6,4,2))
    # print(all_bernoulli(0.5,6,True))
    print(at_least(0.6,5,3,False))
##so that these don't happen on import. only when ran as script.



# todo:
# done - merge the printing and array-collecting functions together.
# add a (least < n) condition for at_least
# ---
# make another calculator for non-bernoulli/changing trials?
