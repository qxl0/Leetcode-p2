class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        arr += [0]
        MOD=10**9+7
        pre,nxt = [-1]*n, [n]*n
        stack = [-1] # increasing 
        for i in range(n+1):
            while len(stack)>1 and arr[stack[-1]]>arr[i]:
                # i is smaller
                top = stack.pop()
                nxt[top] = i
                pre[top] = stack[-1]
            stack.append(i)
        ret = 0
        for i in range(n):
            ret += arr[i]*(i-pre[i])*(nxt[i]-i)
            ret %= MOD
        return ret


        