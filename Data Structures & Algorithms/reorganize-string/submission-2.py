class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        count_s = Counter(s)
        for count in  count_s.values():
            if count > (n+1)//2:
                return ""
        pq=[]
        for char,freq in count_s.items():
            heapq.heappush(pq,(-freq,char))
        
        res=[]
        while pq:
            freq1, char1 = heapq.heappop(pq)
            if res and char1 == res[-1]:
                freq2,char2 = heapq.heappop(pq)
                res.append(char2)
                if freq2+1 < 0:
                    heapq.heappush(pq,(freq2+1,char2))
                heapq.heappush(pq,(freq1,char1))
            
            else:
                res.append(char1)
                if freq1+1 < 0:
                    heapq.heappush(pq,(freq1+1,char1))
        
        return "".join(res)
