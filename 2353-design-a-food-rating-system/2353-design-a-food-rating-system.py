from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        n = len(foods)
        self.dic = {}
        self.temp = {}
        for i in range(n):
            self.temp[foods[i]] = [cuisines[i], ratings[i]]
        
        
        for i in range(n):
            if cuisines[i] not in self.dic:
                self.dic[cuisines[i]] = SortedList()
            self.dic[cuisines[i]].add([ratings[i], foods[i]])
        


    def changeRating(self, food: str, newRating: int) -> None:
        
        cuisine = self.temp[food][0]
        rating = self.temp[food][1]
        self.temp[food][1] = newRating
        self.dic[cuisine].remove([rating, food])
        self.dic[cuisine].add([newRating, food])
        return 
        

    def highestRated(self, cuisine: str) -> str:
        
        rating = self.dic[cuisine][-1][0]
        idx = bisect_left(self.dic[cuisine], [rating ,""])
        return self.dic[cuisine][idx][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)