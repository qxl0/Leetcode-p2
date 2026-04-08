class TrieNode:
    def __init__(self):
        self.next = [None]*2
        self.count = 0
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        '''
        x>=y, x-y<=y => y <= x <= 2*y
        nums.sort()
        loop through array, y, x can go to 2*y
        maintain a trie, keep adding n to trie, 
        calculate possible xor 
        remove it at the end
        two pointers
        '''
        n = len(nums)
        nums.sort()
        root = TrieNode()
        def add(x):
            node = root
            for k in range(31,-1,-1):
                bit = (x>>k)&1 
                if node.next[bit] == None:
                    node.next[bit] = TrieNode()                
                node = node.next[bit]
                node.count += 1
                
        def remove(x):
            node = root
            for k in range(31,-1,-1):
                bit = (x>>k)&1                   
                node = node.next[bit]                            
                node.count -= 1 
        def dfs(x, node, k):
            if k==-1: return 0
            bit = (x>>k)&1            
            if bit==0:
                if node.next[1] and node.next[1].count>0:
                    return dfs(x, node.next[1], k-1)+(1<<k)
                elif node.next[0] and node.next[0].count>0:
                    return dfs(x, node.next[0],k-1)
            else:
                if node.next[0] and node.next[0].count>0:
                    return dfs(x, node.next[0], k-1)+(1<<k)
                elif node.next[1] and node.next[1].count>0:
                    return dfs(x, node.next[1],k-1)
            return 0
        j = 0
        ans = 0
        for i in range(n):            
            while j<n and nums[j]<= 2*nums[i]:
                add(nums[j])
                j += 1
            ans = max(ans, dfs(nums[i], root, 31))
            remove(nums[i])
        return ans
            