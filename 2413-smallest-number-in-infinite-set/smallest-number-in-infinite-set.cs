public class SmallestInfiniteSet {
    private SortedList<int, int> _data = new SortedList<int, int>();
    public SmallestInfiniteSet() {
        for (int i=1;i<=1000;i++) {
            this._data[i] = 1;
        }
    }
    
    public int PopSmallest() {
        int ret = -1;
        if (_data.Count>0) {
            ret = this._data.Keys[0];
            this._data.Remove(ret);
        }
        return ret;
    }
    
    public void AddBack(int num) {
        if (!this._data.ContainsKey(num)) {
            this._data.Add(num, 1);
        }        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.PopSmallest();
 * obj.AddBack(num);
 */