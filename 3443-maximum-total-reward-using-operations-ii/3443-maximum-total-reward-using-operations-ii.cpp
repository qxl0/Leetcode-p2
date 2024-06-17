class Solution {
public:
    int maxTotalReward(vector<int>& A) {
        sort(A.begin(), A.end());
        auto last = unique(A.begin(),A.end());
        A.erase(last,A.end());
        const int N = 5 * 1e4+1;
        bitset<N> dp;

        dp[0] = 1;
        // cout<<dp<<endl;
        for (int i=0;i<A.size()-1;i++) {
            int val = A[i];
            int shift = dp.size()-val;
            // dp: 1101011
            // val: 4
            // shift = 7-4 = 3
            // dp<<shift = 1011000
            // dp<<shift>>shift = 0001011 -> remove the top 3 digits 
            // dp<<shift>>shift<<val = 10110000
            dp |= (dp<<shift>>shift<<val);            
        }
        // cout<<dp.size()<<endl;
        int ret = 0;
        for (int i=dp.size();i>=0; i--) {
            if (dp[i]==1 && i<A.back()){
                ret = i;
                break;
            }

        }
        // cout<<dp<<endl;
        return ret+A.back();
    }
};