class UndergroundSystem:

    def __init__(self):
        
        self.av = {}
        self.cust = {}
        self.time = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.cust[id] = [stationName]
        self.time[id] = [t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        self.cust[id].append(stationName)
        self.time[id].append(t)
        travel = self.cust[id][0]+'-'+stationName
        if  travel in self.av :
            self.av[travel].append(t-self.time[id][0])
        else:
            self.av[travel] = [t-self.time[id][0]]
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        travel = startStation+"-"+endStation
        return sum(self.av[travel])/len(self.av[travel])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)