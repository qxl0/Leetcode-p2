class Twitter:
    t = 0
    def __init__(self):
        self.follows = defaultdict(list)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t += 1
        self.tweets[userId].append((self.t, tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        for uId in self.follows[userId]+[userId]:
            for i,tw in self.tweets[uId]:
                ret.append((i,tw))
        ans = []
        ret.sort()
        for i,t in ret[::-1]:
            if t not in ans:
                ans.append(t)
            if len(ans)==10:
                break
        return list(ans)

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)