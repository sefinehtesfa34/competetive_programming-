class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for index in range(len(heights) + 1):
            while stack and (index == len(heights) or heights[stack[-1]] > heights[index]):
                width = heights[stack.pop()]
                length = (index - 1) - (stack[-1] if stack else -1)
                max_area = max(max_area, width * length)
            stack.append(index)
        return max_area
    