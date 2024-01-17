class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        count2 = Counter(count.values())
        _,freq = count2.most_common()[0]
        return freq==1