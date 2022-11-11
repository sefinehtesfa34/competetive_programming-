class Solution {
public:
    string removeDuplicates(string s) {
        string result;
        for (int index = 0; index < s.size(); index ++){
            if (!result.empty() and s[index] == result.back()){
                result.pop_back();
                }   
            
            else{
                result.push_back(s[index]);
            }
            }
        
        return result;
    }
};