#include <iostream>
using namespace std;
int change(int amount, vector<int>& coins) {
        vector<int>dp(amount + 1, 0);
        dp[0] = 1;
        for (int cur = 1; cur <= amount; cur++){
            for (int index =0; index < coins.size(); index++){
                if (coins[index] <= cur){
                    dp[cur] += dp[cur - coins[index]];
                }
            }
        }
        cout<<dp[amount];
        return 0;
    }
int main(){
    int amount, n;
    int coins[101];
    cin>>n;

}
