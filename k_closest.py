class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        l1=[]
        for i in points:
            l.append((i[0]**2)+(i[1]**2))
        for i in range(k):
            mn=min(l)
            index=l.index(mn)
            l1.append(points[index])
            points.pop(index)
            l.pop(index)
        return l1