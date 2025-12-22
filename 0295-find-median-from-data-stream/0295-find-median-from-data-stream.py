class MedianFinder:

    def __init__(self):
        self.maxH,self.minH = [],[]

    def addNum(self, num: int) -> None:
        #  maxH | minH   
        #   L      R
        heappush(self.minH,num)
        x = heappop(self.minH)
        heappush(self.maxH, -x) 
        if len(self.maxH) > len(self.minH) + 1:
            # --> R    
            x = heappop(self.maxH)
            heappush(self.minH, -x)

    def findMedian(self) -> float:
        if len(self.maxH)==len(self.minH):
            x,y = self.maxH[0], self.minH[0]
            x = -x
            return (x+y)/2
        else:
            return -self.maxH[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()