# given a 6x6 array, find the "hourglass" with
# max sum of its integers. An hourglass is
# defined as a 3 x 1 x 3 "I" shaped slice of
# the array.

# calculate array using arbitrary notation in example
def cal(arr,i,j):
    a=arr[i][j]
    b=arr[i][j+1]
    c=arr[i][j+2]
    d=arr[i+1][j+1]
    e=arr[i+2][j]
    f=arr[i+2][j+1]
    g=arr[i+2][j+2]
    return (a+b+c+d+e+f+g)

if __name__ == '__main__':
    # start empty array
    arr = []
    # take in input
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # calculate the hourglasses
    res=[]
    for i in range(len(arr)-2): # max 4 per row (6 - 2)
        for j in range(len(arr)-2): 
            summ=cal(arr,i,j)
            res.append(summ)
    print(max(res))
