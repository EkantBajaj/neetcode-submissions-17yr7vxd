class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res  = []
        self.followMap[userId].add(userId)
        minHeap = []
        for followee in self.followMap[userId]:
            index = len(self.tweetMap[followee])-1
            if index >= 0:
                minHeap.append([self.tweetMap[followee][index][0],self.tweetMap[followee][index][1],followee,index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            cnt,tweetId,followee,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >=0:
                heapq.heappush(minHeap,[self.tweetMap[followee][index][0],self.tweetMap[followee][index][1],followee,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
