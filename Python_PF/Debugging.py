def multiply(arr,num):
    for x in range(len(arr)):   # for loop the array arr-length times
        arr[x] *= num           # place new x in original x spot of the array
    return arr


a = [2,4,10,16]
b = multiply(a,5)
print b
