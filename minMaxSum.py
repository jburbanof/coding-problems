def miniMaxSum(arr):
    sumas=[]
    index=0
    for i in range(5):
        sumas.append(sum(arr)-arr[index])
        index+=1
    print (min(sumas),max(sumas))