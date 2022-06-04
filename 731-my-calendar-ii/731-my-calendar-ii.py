from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.dic =  SortedDict()
        
    def book(self, start: int, end: int) -> bool:
        
        if start not in self.dic:
            self.dic[start] = 0
        if end not in self.dic:
            self.dic[end] = 0
            
        self.dic[start] += 1
        self.dic[end] -= 1
        
        curr = 0
        for key in self.dic:
            curr+=self.dic[key]
            if curr>=3:
                self.dic[start] -= 1
                self.dic[end] += 1  
                return False
            
        return True
        


        
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)