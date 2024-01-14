class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxfreq = count.most_common()[0][1]
        freqcount = Counter(count.values())
        # print(maxfreq, freqcount)
        return freqcount[maxfreq]*maxfreq