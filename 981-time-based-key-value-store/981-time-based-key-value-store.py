from sortedcontainers import SortedList

class TimeMap:

    def __init__(self):
        self.dic = {}
        self.temp = {}
        

    def set(self, k: str, v: str, t: int) -> None:
        
        if k not in self.dic :
            self.dic[k] = SortedList()
        self.dic[k].add((t,v))
        
        if k not in self.temp :
            self.temp[k] = SortedList()
        self.temp[k].add(t)
            
    def get(self, k: str, t: int) -> str:
        
        if k in self.dic :
            
            idx = bisect.bisect_right(self.temp[k], t)
            if idx == 0 :
                return ""
            else:
                return self.dic[k][idx-1][1]
        return ""
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)