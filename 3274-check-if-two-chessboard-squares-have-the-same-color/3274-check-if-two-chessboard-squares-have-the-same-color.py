class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def color(x,y):
            xc = ord(x)-ord('a')
            yc = int(y)
            if yc%2==0:
                return xc%2
            else:
                return (xc+1)%2
        x1,y1 = coordinate1[0],coordinate1[1]
        x2,y2 = coordinate2[0],coordinate2[1]

        return color(x1,y1)==color(x2,y2)