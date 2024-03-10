class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        count = Counter()
        def addallsubstring(word,count):
            n = len(word)
            for i in range(n):
                for j in range(i,n):
                    count[word[i:j+1] ]+=1
        for word in arr:
            addallsubstring(word,count)
        ans = ['']*n

        for i in range(n):
            thisc = Counter()
            addallsubstring(arr[i], thisc)
            curcount = count.copy()
            curcount.subtract(thisc)
            for substr, freq in (curcount).items():
                if freq ==0 and (ans[i]=='' or len(ans[i])>len(substr) or len(ans[i])==len(substr) and ans[i]>substr):
                    ans[i] = substr
        
        return ans
