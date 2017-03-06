def odd():
    for i in range(1,1000):
        if i % 2 != 0:
            print i

# odd()

def multi_Five():
    for i in range(5,100):
        if i % 5 == 0:
            print i

# multi_Five()

a = [1, 2, 5, 10, 255, 3]

def sum_List(list):
    i = 0
    for a in list:
        i = i + a
    print i

    # print sum(list)  # one line answer

# sum_List(a)

def avg_List(list):
    i = 0
    for a in list:
        i = i + a
    print i/len(list)

    # print sum(list)/len(list) # one line answer

# avg_List(a)
