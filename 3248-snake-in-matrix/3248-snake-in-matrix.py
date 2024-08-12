class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i,j = 0,0
        for cmd in commands:
            if cmd == 'RIGHT':
                j += 1
            elif cmd == 'LEFT':
                j -= 1                
            elif cmd == 'UP':
                i -= 1
            else:
                i += 1
        return i*n+j