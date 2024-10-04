def LCS (A,B):
    m=len(A)
    n=len(B)

    #initlizing matrix of size(m+1)*(n+1)
    dp=[[0]*(n+1) for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

s1="abcdgh"
s2="abedfhr"

print(LCS(s1,s2))