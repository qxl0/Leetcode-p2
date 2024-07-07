class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:        
        mn = min(enemyEnergies)
        if currentEnergy<mn: return 0
        sm = sum(enemyEnergies)-mn
        return (sm+currentEnergy)//mn