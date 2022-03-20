class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        if pattern[0] == pattern[1] :
            count = text.count(pattern[0])
            return count*(count+1)//2
            
        
        arr1 = []
        arr2 = []
        
        for i in range(len(text)) :
            
            if text[i] == pattern[0] :
                arr1.append(i)
            
            elif text[i] == pattern[1] :
                arr2.append(i)
        
        if len(arr1) > len(arr2) : 
            count = len(arr1)
        
        else :
            count = len(arr2)
        
        for idx in arr1 :
            count += len(arr2) - bisect.bisect_left(arr2, idx)
        
        return count
            
        
        