class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = []
        l , r = 0, len(heights) - 1
        while l < r:
            new_vol = min(heights[l],heights[r])*(r-l)
            volume.append(new_vol)
            if heights[l] < heights[r]:
                l += 1
                
            else:
                r += -1
                
        return max(volume)