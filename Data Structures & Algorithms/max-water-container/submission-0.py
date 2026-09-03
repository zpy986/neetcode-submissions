class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxRes = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            maxRes = max(area, maxRes)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxRes