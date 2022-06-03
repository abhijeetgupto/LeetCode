class Twitter:

    def __init__(self):
        
        self.dic = {}
        self.storage = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.storage.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        if userId not in self.dic:
            self.dic[userId] = {userId}
        
        res = []
        i = len(self.storage)-1
        while i>=0 and len(res)<10:
            if self.storage[i][0] in self.dic[userId]:
                res.append(self.storage[i][1])
            i-=1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.dic:
            self.dic[followerId] = {followerId}
        self.dic[followerId].add(followeeId)
        return
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        try:
            self.dic[followerId].remove(followeeId)
            return  
        except:
            return 
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)