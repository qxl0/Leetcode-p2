class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        top2 = count.most_common(2)
        return [v for v,_ in top2]

        