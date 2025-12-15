class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        diff = [0]*1003
        for num,s,e in trips:
            diff[s] += num
            diff[e] -= num
        total = 0
        for i in range(1001):
            total += diff[i]
            if total > capacity:
                return False
        return True
