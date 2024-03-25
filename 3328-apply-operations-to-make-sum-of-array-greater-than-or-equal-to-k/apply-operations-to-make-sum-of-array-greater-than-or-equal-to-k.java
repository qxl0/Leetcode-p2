class Solution {
    public int minOperations(int k) {
        int m = (int)Math.ceil(Math.sqrt(k));
        return m-1+(k-1)/m ;
    }
}