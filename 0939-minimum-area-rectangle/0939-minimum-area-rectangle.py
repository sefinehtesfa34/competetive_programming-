class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(list)
        left_column = {}
        area = inf
        for x, y in points:
            columns[x].append(y)
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for index, y2 in enumerate(column):
                for curr in range(index):
                    y1 = column[curr] # Y2 > y1 meaning Y2 is above Y1
                    if (y1, y2) in left_column:
                        area = min(area, abs(y2 - y1) * abs(x - left_column[y1, y2]))
                    left_column[y1, y2] = x
                    
        return area if area != inf else 0
    