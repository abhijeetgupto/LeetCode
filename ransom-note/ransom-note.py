class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        
        rs = list(set(ransomNote))
        for char in rs:
            if ransomNote.count(char) > magazine.count(char):
                return False
        
        return True