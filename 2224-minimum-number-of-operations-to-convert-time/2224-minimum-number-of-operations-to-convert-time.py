class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def solve(times, cur_total, cor_total):
            operations = 0
            index = 0
            while cur_total < cor_total:
                while times[index] + cur_total <= cor_total:
                    cur_total += times[index]
                    operations += 1
                if cur_total == cor_total:
                    return operations
                index += 1
            return operations

        times = [60, 15, 5, 1]
        cur_hours, cur_minutes = current.split(":")
        cor_hours, cor_minutes = correct.split(":")
        cur_total = int(cur_minutes) + int(cur_hours)*60
        cor_total = int(cor_minutes) + int(cor_hours)*60
        result = solve(times, cur_total, cor_total)
        return result
    
