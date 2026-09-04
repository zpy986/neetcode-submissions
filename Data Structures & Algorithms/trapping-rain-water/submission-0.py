class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 1
        totalArea = 0
        n = len(height)
        if n< 3:
            return 0

        while left < n:
            right = left + 1
            while right < n and height[right] < height[left] :
                right += 1
            
            if right == n:
                if left + 1 >= n:
                    break

                right = max(
                    range(left + 1, n),
                    key=lambda i: height[i]
                )
            
            area = min(height[left], height[right]) * (right - left - 1)
            if area > 0:
                for i in range(left + 1, right):
                    area -= height[i]
            
            totalArea += area
            left = right
            right += 1
        
        return totalArea