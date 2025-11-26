class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-i for i in stones]
        heapify(arr)
        while len(arr)>=2:
            s1,s2 = heappop(arr), heappop(arr)
            s1,s2 = -s1,-s2
            if s1<s2:
                heappush(arr, s-s12)
            elif s1>s2:
                heappush(arr, s2-s1)
        return -arr[0] if len(arr)==1 else 0
