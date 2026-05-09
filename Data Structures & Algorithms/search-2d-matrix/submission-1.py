class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row in which target may exist
        start = 0
        end = len(matrix)-1
        found = False
        c = len(matrix[0])-1
        while not found and start<=end:
            mid = (start+end)//2

            if matrix[mid][c] >= target >= matrix[mid][0]:
                found = True
            elif target > matrix[mid][c]:
                start =mid+1
            else:
                end = mid-1
        
        if not found:
            return False
        
        l = 0
        r = c

        while l <= r:
            middle = (l+r)//2
            if target == matrix[mid][middle]:
                return True
            elif target > matrix[mid][middle]:
                l = middle+1
            else:
                r = middle-1
        
        return False