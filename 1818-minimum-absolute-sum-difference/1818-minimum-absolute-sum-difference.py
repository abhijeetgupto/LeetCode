class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        temp = sorted(set(nums1))
        n1 = len(temp)
        
        count = 0
        change = [0,0,0]
        
        for i in range(n) :
            
            idx = bisect.bisect_left(temp, nums2[i])
            if idx == n1 :
                m2 = abs(temp[idx-1] - nums2[i])
            elif idx == 0 :
                m2 = abs(temp[idx] - nums2[i])
            else:
                m2 = min(abs(temp[idx-1] - nums2[i]), abs(temp[idx] - nums2[i]))
            
            diff = abs(abs(nums1[i]-nums2[i])-m2)
            if diff > change[0] :
                change = [diff, i, m2]
        
        
                
        for i in range(n) :
            if i == change[1] :
                count += change[2]
            else:
                count += abs(nums1[i]-nums2[i])
                
        return count%1000000007
                
            
        