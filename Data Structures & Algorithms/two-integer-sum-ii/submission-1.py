class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        last= len(numbers)-1
        while start<last:
            if numbers[start]+numbers[last]== target:
                return [start+1, last+1]
            elif numbers[start]+numbers[last]> target:
                last -=1
            else:
                start +=1

            

            
        