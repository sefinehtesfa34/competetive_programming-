using namespace std;
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n + 1, 1);
        for (int index = 1; index < n; index++){
            for (int curr = 0; curr < index; curr++){
                if (nums[index] > nums[curr]){
                    dp[index] = max(dp[index], 1 + dp[curr]);
                }
            }
        }
        return *max_element(dp.begin(), dp.end());
        
    }
};