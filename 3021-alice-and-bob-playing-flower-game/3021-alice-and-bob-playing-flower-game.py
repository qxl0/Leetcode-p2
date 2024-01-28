class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # 1..m how many odds, evens
        m_odds = sum(1 for i in range(1,m+1) if i%2==1)
        m_evens = sum(1 for i in range(1,m+1) if i%2==0)
        
        n_odds = sum(1 for i in range(1,n+1) if i%2==1)
        n_evens = sum(1 for i in range(1,n+1) if i%2==0)
        
        return m_odds*n_evens + m_evens*n_odds
        
        