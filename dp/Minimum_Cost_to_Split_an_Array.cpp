class Solution {
public:
    
    int minCost(vector<int>& nums, int k) {
        vector<int>dp(nums.size() + 1, 0);
        for (int index = nums.size() - 1; index >=0; index--){
            int cur_count = 0;
            unordered_map<int, int>hashmap;
            dp[index] = k + nums.size();
            for (int right = index; right < nums.size(); right ++){
                hashmap[nums[right]] += 1;
                if (hashmap[nums[right]] == 2){
                    dp[index] = min(dp[index], 2 + cur_count + k + dp[right + 1]);
                    cur_count += 2;
                }
                else if (hashmap[nums[right]] > 2){
                    dp[index] = min(dp[index], 1 + k + cur_count + dp[right + 1]);
                    cur_count += 1;
                }
                else {
                    dp[index] = min(dp[index], k + cur_count + dp[right + 1]);
                }
            }
        }
        return dp[0];
    }
};