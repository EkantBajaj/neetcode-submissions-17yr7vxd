class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        i=0
        j=len(heights)-1

        while i < j:
            maxWater = max(maxWater,min(heights[i],heights[j])*(j-i))
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return maxWater