class BrowserHistory:

    def __init__(self, homepage: str):
        self.arr = [homepage]
        self.curr = 0
        
    def visit(self, url: str) -> None:
        self.arr = self.arr[ :self.curr+1]
        self.arr.append(url)
        self.curr = len(self.arr)-1
        
    def back(self, steps: int) -> str:
        while self.curr>0 and steps != 0:
            self.curr -= 1
            steps -= 1
        return self.arr[self.curr]
        
        
    def forward(self, steps: int) -> str:
        while self.curr < len(self.arr) and steps != 0:
            self.curr += 1
            steps -= 1
        if self.curr == len(self.arr):
            self.curr -= 1
        return self.arr[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)