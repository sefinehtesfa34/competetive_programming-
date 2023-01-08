class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums =  set(arr)
        max_val = max(arr)
        longest = 0
        for index in range(len(arr)):
            for curr in range(index + 1, len(arr)):
                a, b = arr[index], arr[curr]
                cur_longest = 0
                c = 0
                c = a + b
                while c <= max_val and c in nums:
                    a = b
                    b = c
                    c = a + b
                    cur_longest += 1
                if cur_longest:
                    cur_longest += 2
                longest = max(cur_longest, longest)
        return longest
    