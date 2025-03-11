class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        placed = [False]*n
        cnt = 0
        for i in range(n):
            cur = fruits[i]
            for j in range(n):
                if placed[j]:
                    continue
                if cur>baskets[j]:
                    continue
                placed[j] = True
                # print(f'placed: {fruits[i]} at {j}')
                cnt += 1
                break
        return n-cnt
