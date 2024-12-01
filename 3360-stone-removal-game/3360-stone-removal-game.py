class Solution:
    def canAliceWin(self, n: int) -> bool:
        def helper(x, player, turn):  
            # turn==1, player=0, remove 10, helper(x-10, 'B', 1-turn)
            if x>=10-turn:
                return helper(x-10+turn, 1-player, turn+1)
            else:
                if player==0:
                    return False
                else:
                    return True
        return helper(n, 0, 0)
