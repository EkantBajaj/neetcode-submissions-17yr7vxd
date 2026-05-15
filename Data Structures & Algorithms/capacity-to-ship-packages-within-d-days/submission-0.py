class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) #min capacity required in ship
        r = sum(weights) #max capacity that ship can hold in a day

        res = r
        while l<=r:
            mid = (l+r)//2

            i = 0
            days_taken = 0
            while i<len(weights):
                capacity = mid
                while i<len(weights) and capacity >= weights[i]:
                    capacity-=weights[i]
                    i+=1
                days_taken +=1
            
            if days_taken <= days:
                res = min(res,mid)
                r = mid-1
            else:
                l = mid + 1
        return res