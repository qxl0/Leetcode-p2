class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        m = len(units)
        n = len(units[0])
        if n == 1:
            return sum(*zip(*units))
        global_min = inf
        second_min_lst = []
        for i in range(m):
            temp_l = sorted(units[i])            
            second_min_lst.append(temp_l[1])
            global_min = min(global_min, temp_l[0])
        second_min_lst.sort()
        return global_min+sum(second_min_lst[1:])
            


