class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        n = len(words)
        
        
        
        def word_score(word) :
            
            res = 0
            for char in word :
                res += score[ord(char)-97]
            return res
        
        def possible(word, taken) :
            
            dic = dict(collections.Counter(letters))
            for char in taken :
                dic[char] -= 1
            
            temp = dict(collections.Counter(word))
            for key in temp :
                if (key not in dic) or (dic[key] < temp[key]) :
                    return False
                
            return True
        
        
        
        def rec(i=0, taken = []) :
            
            if i>=n:
                return 0
            
            else:
                
                if possible(words[i], taken) :
                    return max(word_score(words[i]) + rec(i+1, taken+list(words[i])), rec(i+1,taken))
                
                return rec(i+1, taken)
        
        return rec()
                    
                    
                
                
        
        
        
                
        
        
        