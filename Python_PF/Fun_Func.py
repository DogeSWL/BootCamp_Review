def odd_Even():
    for i in range(1,201):
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number".format(i)

# odd_Even()

a = [2,4,10,16]

def multi(list,num):
    newL = []

    for i in list:
        a = i * num
        newL.append(a)

    return newL

# multi(a,5)


def layered_Multi(arr):
    newArr = []

    for i in arr:
        tempArr = []
        
        while i > 0:
            tempArr.append(1)
            i = i-1

        newArr.append(tempArr)

    return newArr

print layered_Multi(multi([2,4,5],3))
