class TopVotedCandidate:

    def __init__(self, votes: List[int], time: List[int]):
        
        count = {}
        dic = {}
        curr_max = None

        for i in range(len(time)):
            if votes[i] in count:
                count[votes[i]] += 1
            else :
                count[votes[i]] = 1

            if curr_max is None :
                dic[time[i]] = votes[i]
                curr_max = votes[i]

            else :
                if count[curr_max] > count[votes[i]]:
                    dic[time[i]] = curr_max
                else :
                    dic[time[i]] = votes[i]
                    curr_max = votes[i]

        self.dic = dic
        self.time = time

    def q(self, t: int) -> int:
        
        idx = bisect.bisect_right(self.time,t)
        return self.dic[self.time[idx-1]]
        
        
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)