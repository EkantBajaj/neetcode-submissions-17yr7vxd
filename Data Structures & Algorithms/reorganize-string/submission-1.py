class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        
        freq = Counter(s)
        n= len(s)

        for count in  freq.values():
            if count > (n+1)//2:
                return ""
        
        pq=[]
        for ch,count in freq.items():
            heapq.heappush(pq, (-count,ch))
        
        res = []
        while pq:
            count1,ch1 = heapq.heappop(pq)

            if res and res[-1]==ch1:
                count2,ch2 = heapq.heappop(pq)
                res.append(ch2)
                if count2+1 < 0:
                    heapq.heappush(pq,(count2+1,ch2))
                heapq.heappush(pq,(count1,ch1))
            else:
                res.append(ch1)
                if count1+1 < 0:
                    heapq.heappush(pq,(count1+1,ch1))
        
        return "".join(res)