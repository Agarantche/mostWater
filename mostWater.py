class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            currentHeight = min(heights[left], heights[right])
            currentWidth = right - left
            currentArea = currentHeight * currentWidth

            if currentArea > maxArea:
                maxArea = currentArea
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] <= heights[left]:
                right -= 1
            
        return maxArea
