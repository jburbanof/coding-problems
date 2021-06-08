def diagonalDifference(arr):
    i = 0
    j = 0
    diag1=0
    diag2=0
    diagdif=0
    
    for x in range (0,n-1):
        diag1+= arr[x][x]
    diag1+=arr[n-1][n-1]
    for y in range(n-1):
        diag2+=arr[y][(n-1)-y]
    diag2+=arr[n-1][0]
    
    return abs(diag1-diag2)