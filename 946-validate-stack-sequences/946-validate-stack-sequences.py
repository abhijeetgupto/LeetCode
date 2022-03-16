class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        temp = []
        i = 0
        j = 0
        
        while i<len(pushed) and j<len(popped) :
            
            temp.append(pushed[i])
            i += 1
            
            while temp and j<len(popped) and temp[-1] == popped[j] :
                j+=1
                temp.pop()
        
        return len(temp)==0
        