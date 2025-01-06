class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # get the largest id  
        maxid = max(max(f,to) for f, to, _ in transactions)
        help = [0]*(maxid+1)
        for f,t,amount in transactions:
            help[f] -= amount
            help[t] += amount
        # remove any 0 from help
        arr = []
        for x in help:
            if x==0:
                continue
            arr.append(x)
        n = len(arr)
        # ans = len(arr)- f(arr,set)
        dp = [-1]*(1<<n)
        def f(s, sum):
            if dp[s]!=-1:
                return dp[s]
            ans = 0
            if (s&(s-1)!=0): # s : contains more than 1 
                if sum==0:
                    for i in range(n):
                        if s&(1<<i)!=0:
                            ans = f(s^(1<<i), sum-arr[i])+1
                            break
                else:
                    for i in range(n):
                        if (s&(1<<i)!=0):
                            ans = max(ans, f(s^(1<<i), sum-arr[i]))
            dp[s]=ans
            return ans
        return n - f((1<<n)-1, 0)