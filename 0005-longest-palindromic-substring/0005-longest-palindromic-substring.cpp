class Solution {
public:
    
    string longestPalindrome(string s) {
        int best_left = 0, best_right = 0;
        vector<vector<int>> dp(s.size(), vector<int>(s.size(), 0));
        
        for (int index = 0; index < s.size(); index ++){
            dp[index][index] = 1;
        }
        
        for (int row = 1; row < s.size(); row ++ ){
            for (int col = 0; col < row; col ++){
                if (row - 1 == col){
                    dp[row][col] = (s[row] == s[col]);
                }
                else{
                    dp[row][col] = dp[row - 1][col + 1] && s[row] == s[col];
                }
                
                if (dp[row][col] == 1){
                    if(best_right - best_left < row - col){
                        best_right = row;
                        best_left = col;
                    }
                }
            }
        }
        return s.substr(best_left, best_right - best_left + 1);
    }
};