class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        _,fmax = count.most_common()[0]
        p = Counter(count.values())[fmax]
        return max(len(tasks), (fmax-1)*(n+1)+p)