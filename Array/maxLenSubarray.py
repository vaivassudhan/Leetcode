#Dynamic programming Approach 
# Since common subarray of A[] and B[] must start at some index i and j such that A[i] is equals to B[j]. Let dp[i][j] be the longest common subarray of A[i…] and B[j…].
# Therefore, for any index i and j, if A[i] is equals to B[j], then dp[i][j] = dp[i+1][j+1] + 1.
# The maximum of all the element in the array dp[][] will give the maximum length of equal subarrays.
def findLength(a,b):
    print(a)
    n=len(a)
    m=len(b)
    dp=[[0]*(n+1)]*(m+1)
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if(a[i]==b[j]):
                dp[j][i]=1+dp[j+1][i+1]
    maxv=0
    for i in range(n):
        for j in range(m):
            print(dp[i][j],end=" ")
            maxv=max(maxv,dp[i][j])
        print()
    return maxv



a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(findLength(a,b))