from itertools import accumulate


class Solution:
    def range_sum(self):
        queries = self.get_query()
        nums = self.get_nums()
        # Build the binary indexed tree
        tree = self.build_tree(nums)
        # Find the range sum for the current query
        for query in queries:
            start = query[0]
            end = query[1]
            print(self.sum_query(end, tree) - self.sum_query(start - 1, tree))
             
    def build_tree(self, nums):
        # tree[k] = SUMq(k - p(k) + 1,k)
        # where  P(k) is the largest power of two that divides k
        # tree[k] = SUMq(1, k) - SUMq(1, k - p(k))
        # p(k) = k&-k
        # prefix_sum = list(accumulate(nums, initial= 0))
        tree = [0]*(len(nums) + 1)
        for k in range(len(nums)):
            self.update(tree, k, nums[k])
        return tree 
    
    def update(self, tree, k, x):
        while (k <= len(tree)):
            tree[k] += x 
            k +=( k & -k )
        return tree 
        
        
    def sum_query(self, k, tree):
        current_sum = 0
        while  k >=1:
            current_sum += tree[k]
            k -= k & -k 
        return current_sum 
    
    def get_query(self):
        num_queries = int(input())
        queries = []
        for _ in range(num_queries):
            queries.append(list(map(int, input().split())))
        return queries 
    
    def get_nums(self):
        return list(map(int, input().split()))
    
        
solution = Solution()
solution.range_sum()
# 1 3 4 8 6 1 4 2

        
        
        
        
    
        
        
        
    
            