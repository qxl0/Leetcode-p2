class Solution {
public:
    int maxTotalReward(vector<int>& A) {
        sort(A.begin(), A.end());
        const int N = 100001;
        bitset<N> dp;

        dp[0] = 1;

        for (int i=0;i<A.size();i++) {
            int val = A[i];
            int shift = dp.size()-val;
            dp |= (dp<<shift>>shift<<val);            
        }
        int pos = dp.to_string().find('1');
        return dp.size()-pos-1;
    }
};