class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def solve(n1,n2):
            height = 0
            cur = 1 
            size = 1           
            while n1>0 or n2>0:
                if cur==1:
                    if n1>=size:
                        n1 -= size                         
                        cur = 2                        
                    else:
                        break
                else: # cur==2
                    if n2>=size:
                        n2 -= size                        
                        cur = 1
                    else:
                        break                
                size += 1
                height += 1
            return height

        h = 0
        h = max(h, solve(red,blue))
        h = max(h, solve(blue,red))
        return h

