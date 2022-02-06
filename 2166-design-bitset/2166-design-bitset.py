class Bitset:

    def __init__(self, size: int):
        
        self.l = ["ones", set()]
        self.size = size

    def fix(self, idx: int) -> None:
        
        if self.l[0] == "ones" :
            self.l[1].add(idx)
        
        else:
            if idx in self.l[1] :
                self.l[1].remove(idx)

        
    def unfix(self, idx: int) -> None:
        
        if self.l[0] == "ones" :
            if idx in self.l[1] :
                self.l[1].remove(idx)
        else:
            self.l[1].add(idx)
            
        
    def flip(self) -> None:
        
        if self.l[0] == "ones" :
            self.l[0] = "zeros"
        else:
            self.l[0] = "ones"
        
    def all(self) -> bool:
        
        if self.l[0] == "ones" :
            return  len(self.l[1]) == self.size 
        
        else:
            return len(self.l[1]) == 0
            

    def one(self) -> bool:
        
        if self.l[0] == "ones" :
            return len(self.l[1])>0
        
        else:
            return len(self.l[1])<self.size
        
        
    def count(self) -> int:
        
        if self.l[0] == "ones" :
            return len(self.l[1])
        
        else:
            return self.size - len(self.l[1])

    def toString(self) -> str:
        
        
        if self.l[0] == "ones" :
            res = ""
            for i in range(self.size) :
                if i in self.l[1] :
                    res += "1"
                else:
                    res += "0"
            return res
        else:
            res = ""
            for i in range(self.size) :
                if i in self.l[1] :
                    res += "0"
                else:
                    res += "1"
            return res