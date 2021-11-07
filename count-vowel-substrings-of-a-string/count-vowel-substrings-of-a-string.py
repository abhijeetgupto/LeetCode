class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        count = 0
        compare = {'a','e','i','o','u'}
        for i in range(len(word)-4):
            s = set(word[i:i+5])
            if s==compare:
                count+=1
            for j in range(i+5,len(word)):
                s.add(word[j])
                if s==compare :
                    count+=1
        return count
            
            