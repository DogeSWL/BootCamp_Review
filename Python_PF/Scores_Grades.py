import random

def genGrade():
    a = random.randint(60,100)

    if a <= 69:
        return "Score:%s; Your Grade is D" % a
    elif a >= 70 and a <= 79:
        return "Score:%s; Your Grade is C" % a
    elif a >= 80 and a <= 89:
        return "Score:%s; Your Grade is B" % a
    else:
        return "Score:%s; Your Grade is A" % a

def run10():
    for i in range(10):
        print genGrade()
    return  "End of program. Bye!"

print run10()
