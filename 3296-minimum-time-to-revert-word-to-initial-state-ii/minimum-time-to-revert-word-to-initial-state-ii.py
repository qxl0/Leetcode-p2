class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        z = [0]*n  # z[i]: # represents the length of the longest substring starting from i that is also a prefix of s
       
        l=r=0
        for i in range(1,n):
            if i<r:
                z[i] = min(z[i-l], r-i)
                
            while i+z[i]<n and word[z[i]]==word[i+z[i]]:
                z[i] += 1
            if i+z[i]>r:
                l = i
                r = i+z[i]
        print(z)
        for i in range(k, n, k):
            if z[i]==n-i:
                return i//k
        return (n+k-1)//k