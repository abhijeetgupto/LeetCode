import sortedcontainers

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        
        self.t = timeToLive
        self.dic = {}
        self.l = sortedcontainers.SortedList()

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        x = currentTime + self.t
        self.dic[tokenId] = x
        self.l.add(x)
        
    
    def renew(self, tokenId: str, currentTime: int) -> None:
        
        if tokenId in self.dic and self.dic[tokenId] > currentTime : 
            x = self.dic[tokenId]
            self.l.remove(x)
            self.dic[tokenId] = currentTime + self.t
            self.l.add(currentTime + self.t)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:

        idx = bisect.bisect_right(self.l,currentTime)
        return len(self.l)-idx
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)