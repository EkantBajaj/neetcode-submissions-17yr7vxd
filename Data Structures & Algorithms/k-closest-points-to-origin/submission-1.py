class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceHeap = []

        for index, value in enumerate(points):
            distance = value[0]**2 +value[1]**2
            heapq.heappush(distanceHeap,(distance,index))
        result = []
        for _ in range(k):
            dist,index = heapq.heappop(distanceHeap)
            result.append(points[index])
        
        return result