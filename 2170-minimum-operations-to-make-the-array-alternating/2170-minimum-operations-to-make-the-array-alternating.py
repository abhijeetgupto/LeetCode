from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        
        def checker(n1,n2) : 
            count = 0
            for i in range(len(nums)) :
                if i%2==0:
                    if nums[i]!=n2:
                        count+=1
                else:
                    if nums[i]!=n1:
                        count+=1
            return count

        odd = [nums[i] for i in range(1,len(nums),2)]
        even = [nums[i] for i in range(0,len(nums),2)]
        
        x1 = Counter(odd).most_common()  #odd
        x2 = Counter(even).most_common() #even
        
        n1 = x1[0][0]
        n2 = x2[0][0]
        
        if n1 != n2 :
            return checker(n1,n2)

        else:
            if len(x1)==1 and len(x2)==1:
                return len(nums)//2
            
            elif len(x1) >= 2 and len(x2) >= 2 :
                
                if x1[1][1] > x2[1][1] :
                    return checker(x1[1][0], n2)
                else:
                    return checker(n1, x2[1][0])
                
            elif len(x1)==1:
                return checker(n1, x2[1][0])
                
            elif len(x2)==1 :
                return checker(x1[1][0], n2)
                
                
        
        