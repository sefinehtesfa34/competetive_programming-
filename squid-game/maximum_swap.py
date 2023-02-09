class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        cur_max = '0'
        cur_index = 0
        dp = [0]*(len(num))
        for index in range(len(num)-1, -1, -1):
            if num[index] > cur_max:
                cur_index = index
                cur_max = num[index]
            dp[index] = cur_index
        for index in range(len(num)):
            if dp[index] > index and num[dp[index]] > num[index]:
                num[index], num[dp[index]] = num[dp[index]], num[index]
                return int("".join(num))
        return int("".join(num))
    
            