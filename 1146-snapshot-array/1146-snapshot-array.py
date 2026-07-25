class SnapshotArray:

    def __init__(self, length: int):
        self.n = length        
        self.snaps = [[[-1,0]] for _ in range(self.n)]
        self.snapId = 0
        

    def set(self, index: int, val: int) -> None:
        # set val at index to val
        last = self.snaps[index][-1]
        if last[0] == self.snapId:
            last[1] = val
        else:
            self.snaps[index].append([self.snapId, val])        

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        # get 
        pos = bisect_right(self.snaps[index], [snap_id, inf])
        s_i, s_v = self.snaps[index][pos-1]
        return s_v


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)