class UndergroundSystem:

    def __init__(self):  
        self.start = {}
        self.data = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id] = [stationName,t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.start[id][0]
        t1 = self.start[id][1]
        
        if (start_station, stationName) not in self.data:
            self.data[(start_station, stationName)] = [0,0]
        
        self.data[(start_station, stationName)][0] += (t-t1)
        self.data[(start_station, stationName)][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        l = self.data[(startStation, endStation)]
        return l[0]/l[1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)