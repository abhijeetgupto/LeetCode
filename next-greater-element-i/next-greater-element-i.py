class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=[]
        for number in nums1:
            out.append(self.nextgreater(number,nums2))
        return out
     
    def nextgreater(self,num,l):
        index=l.index(num)
        if index==len(l):
            return -1
        
        for i in range(index+1,len(l)):
            if l[i]>l[index]:
                return l[i]
        
        return -1
            