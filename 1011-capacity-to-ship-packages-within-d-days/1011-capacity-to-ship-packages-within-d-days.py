class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def num_days(capacity):
            cap = 0
            num = 1
            for index in range(len(weights)):
                if weights[index] > capacity:
                    return sum(weights)
                if cap + weights[index] > capacity:
                    cap = 0
                    num += 1
                cap += weights[index]
            return num
        high = sum(weights)
        low = 0
        while low < high:
            mid = (low + high) // 2
            cur_days = num_days(mid)
            if cur_days <= days:
                high = mid
            else:
                low = mid + 1
        return high
    
    
        
        
        
        