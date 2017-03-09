import random

def RunTimes(x):
    headCount = 0
    tailCount = 0
    
    for i in range(x):
        a = round(random.random())
        currCount = i + 1

        if a > 0:
            headCount += 1
            print "Attempt #%s: Throwing coin...It's a Head!...Head(s): %s : Tail(s): %s" % (currCount, headCount, tailCount)
        else:
            tailCount += 1
            print "Attempt #%s: Throwing coin...It's a Tail!...Head(s): %s : Tail(s): %s" % (currCount, headCount, tailCount)

RunTimes(5)
