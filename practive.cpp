class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int dp[nums.size()];
        dp[0]=nums[0];
        int sum=dp[0];
        if(nums[0]<0)sum=0; //as the minimum sum that can be returned is 0
		for(int i=1;i<nums.size();++i){
            sum+=nums[i];
            if(sum>dp[i-1])dp[i]=sum;
            else dp[i]=dp[i-1];
            if(sum<0) sum=0;
        }
        return dp[nums.size()-1];
    }
};