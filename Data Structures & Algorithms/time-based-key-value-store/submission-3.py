class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.timemap[key]
        if values:
            l=0
            r=len(values)-1
            while l<=r:
                mid = (l+r)//2
                if values[mid][0]==timestamp:
                    return values[mid][1]
                if values[mid][0]<timestamp:
                    l=mid+1
                else:
                    r=mid-1
            return values[r][1] if r>=0 else ""
        else:
            return ""
        
