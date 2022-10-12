'''
Recently, Pari and Arya did some research about NP-Hard problems and they found the minimum vertex cover problem very interesting.

Suppose the graph G is given. Subset A of its vertices is called a vertex cover of this graph, 
if for each edge uv there is at least one endpoint of it in this set, i.e.  or  (or both).
Pari and Arya have won a great undirected graph as an award in a team contest. 
Now they have to split it in two parts, but both of them want their parts of the graph to be a vertex cover.
They have agreed to give you their graph and you need to find two disjoint subsets of its vertices A and B, 
such that both A and B are vertex cover or claim it's impossible. 
Each vertex should be given to no more than one of the friends (or you can even keep it for yourself).
Input
The first line of the input contains two integers n and m (2 ≤ n ≤ 100 000, 1 ≤ m ≤ 100 000) — the number of vertices and the number of edges in the prize graph, respectively.

Each of the next m lines contains a pair of integers ui and vi (1  ≤  ui,  vi  ≤  n), denoting an undirected edge between ui and vi. It's guaranteed the graph won't contain any self-loops or multiple edges.

Output
If it's impossible to split the graph between Pari and Arya as they expect, print "-1" (without quotes).

If there are two disjoint sets of vertices, such that both sets are vertex cover, print their descriptions. Each description must contain two lines. The first line contains a single integer k denoting the number of vertices in that vertex cover, and the second line contains k integers — the indices of vertices. Note that because of m ≥ 1, vertex cover cannot be empty.

Examples

'''
from typing import Counter
def findSubarrays(nums, k):
    counter = Counter()
    numSubarrays = left = 0
    for index, num in enumerate(nums):
        counter[num] += 1
        n = len(nums)
        while counter[num] == k and left <= index:
            numSubarrays += n - index
            counter[nums[left]] -= 1
            left += 1
    return numSubarrays
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(findSubarrays(nums, k))

    