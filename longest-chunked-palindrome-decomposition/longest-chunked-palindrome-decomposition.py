class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        count = 0
        text = list(text)
        
        flag = False
        curr1 = ""
        curr2 = ""
        
        flag2 = True
        
        while text :
            
            if len(text) == 1 :
                flag2 = False
                count += 1
                break
                
            if not flag :
                front = text.pop(0)
                back = text.pop()
                
                if front == back :
                    count += 2
                
                else:
                    curr1 = front
                    curr2 = back
                    flag = True
                    
            else :
                front = text.pop(0)
                back = text.pop()
                
                curr1 += front
                curr2 = back+curr2
                
                if curr1 == curr2:
                    count += 2
                    curr1 = ""
                    curr2 = ""
                    flag = False
                    
        if curr1 and curr2 and flag2 :
            count+=1
        return count
                
                    
                
            
        
        