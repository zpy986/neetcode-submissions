class Twitter:

    def __init__(self):
        self.followmap = defaultdict(set)
        self.tweetmap = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.count, tweetId))
        self.count += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        if userId in self.tweetmap:
            for time, tweet in self.tweetmap[userId]:
                heapq.heappush(heap, (time, tweet))
                if len(heap) > 10:
                    heapq.heappop(heap)
        if userId in self.followmap:
            for followeeId in self.followmap[userId]:
                for time, tweet in self.tweetmap[followeeId]:
                    heapq.heappush(heap, (time, tweet))
                    if len(heap) > 10:
                        heapq.heappop(heap)
        res = []
        while heap:
            time, tweet = heapq.heappop(heap)
            res.append(tweet)
        
        res.reverse()
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)

