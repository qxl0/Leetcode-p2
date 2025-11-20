class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        @lru_cache(None)
        def helper(i): # max pts [i...n]
            if i>=n:
                return 0
            ret = max(helper(i+1), questions[i][0]+helper(i+questions[i][1]+1))
            return ret
        return helper(0)