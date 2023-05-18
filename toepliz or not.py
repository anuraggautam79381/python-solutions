def istoepliz(lis,n,m):
    for i in range(0,n-1):
        for j in range(0,m-1):
            if lis[i][j]==lis[i+1][j+1]:
                continue
            else:
             return 0
    return 1    