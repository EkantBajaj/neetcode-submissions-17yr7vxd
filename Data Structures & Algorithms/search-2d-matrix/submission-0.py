class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row =0
        maxRow = len(matrix)-1
        maxCol = len(matrix[0])-1

        while row <= maxRow and target > matrix[row][maxCol]:
            row+=1
        if row > maxRow:
            return False
        
        l=0
        r=maxCol

        while l<=r :
            mid = l+(r-l)//2
            if matrix[row][mid]==target:
                return True
            elif target > matrix[row][mid]:
                l = mid+1
            else:
                r = mid-1
        return False

        