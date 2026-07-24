class SnapshotArray:

    def __init__(self, length: int):
        self.n = length
        self.vals = [0]*self.n
        self.snaps = [[(-1,0)] for _ in range(self.n)]
        self.snapId = 0
        self.changed = set()

    def set(self, index: int, val: int) -> None:
        # set 
        self.vals[index] = val
        self.changed.add(index)

    def snap(self) -> int:
        # take snapshot
        for i in self.changed:
            self.snaps[i].append((self.snapId, self.vals[i]))
        self.snapId += 1
        self.changed.clear()
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        # get 
        pos = bisect_right(self.snaps[index], (snap_id, inf))
        s_i, s_v = self.snaps[index][pos-1]
        return s_v


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)