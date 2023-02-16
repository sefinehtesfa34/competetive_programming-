class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(ci, curr_running_char, curr_running_char_count, remains):
            
            if ci == len(s):
                return 0
            
            
            delete_char_distance = inf
            if remains > 0:
                delete_char_distance = dp(ci+1, curr_running_char, curr_running_char_count, remains - 1)
            
            curr_letter = s[ci]
            
            keep_ch_cost = inf
            if curr_letter == curr_running_char:
                # same letter as previous
                add = 0
                
                # if curr_running_char_count == 1 , since we donot add a1 but only a2, 
                if curr_running_char_count == 1 or len(str(curr_running_char_count + 1)) > len(str(curr_running_char_count)):
                    add = 1
                
                keep_ch_cost = add + dp(ci+1, curr_letter, curr_running_char_count + 1, remains)
            else:
                # different letter
                keep_ch_cost = 1 + dp(ci+1, curr_letter, 1, remains)
            
            return min(keep_ch_cost, delete_char_distance)
                
            
        res = dp(0, "", 0, k)
        return res