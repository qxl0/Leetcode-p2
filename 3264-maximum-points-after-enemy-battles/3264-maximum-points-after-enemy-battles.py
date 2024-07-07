class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:    
        """ If you have at least 1 point, you can choose an unmarked enemy
                                ^^^^, this is point, not energy 
        """
        mn = min(enemyEnergies)
        if currentEnergy<mn: return 0
        sm = sum(enemyEnergies)-mn
        return (sm+currentEnergy)//mn