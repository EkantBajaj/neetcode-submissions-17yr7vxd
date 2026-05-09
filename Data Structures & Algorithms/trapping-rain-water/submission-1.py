class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)

        maxHeight= height[0]
        for i in range(len(height)):
            if maxHeight < height[i]:
                maxHeight = height[i]
            left[i]=maxHeight
        
        maxHeight = height[-1]
        for i in range(len(height)-1,-1,-1):
            if maxHeight < height[i]:
                maxHeight=height[i]
            right[i]=maxHeight
        
        res = 0
        for i in range(len(height)):
            res += min(left[i],right[i])-height[i]
        
        return res
