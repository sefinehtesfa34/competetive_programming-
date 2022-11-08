#include <iostream>
#include <string.h>
int main(){
    int test;
    std::cin >> test;
    for (int i = 0; i < test; i++){
        int n;
        std::cin >> n;
        std::string arr;
        std::cin >> arr;
        unsigned long long left, right, longest;
        longest = 0;
        right = 0;
        left = 0;
        unsigned long long cur_max = 0;
        while (right < n){
            if (arr[right] == '0'){
                left = right + 1;
            }
            if (right - left + 1 > longest){
                longest = right - left + 1;
            }
            right++;
            }

        if (longest * longest > cur_max){
            cur_max = longest * longest;
            } 
            
        unsigned long long lf, rt, lg;
        lg = 0;
        rt = 0;
        lf = 0;
        while (rt < n){
            if (arr[rt] == '1'){
                lf = rt + 1;
            }
            if (rt - lf + 1 > lg){
                lg = rt - lf + 1;
            }
            rt++;
            }

        if (lg * lg > cur_max){
            cur_max = lg * lg;
        }
        unsigned long long ones = 0;
        unsigned long long zeros = 0;
        for (int i = 0; i < n; i++ ){
            if (arr[i] == '1'){
                ones ++;
            } 
            else{
                zeros ++;
            }
        }
        if (cur_max < ones * zeros){
            cur_max = ones * zeros;
        }
        if (ones == 0){
            std::cout << zeros * zeros << "\n";
        }
        else if(zeros == 0){
            std::cout << ones * ones << "\n";
        }
        else{
        
        std::cout << cur_max <<"\n";
        }       
    }
    
    return 0;

}