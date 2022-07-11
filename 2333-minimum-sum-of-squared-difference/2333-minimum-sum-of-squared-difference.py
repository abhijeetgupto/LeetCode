class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        
        
        temp = []
        for i in range(len(nums1)):
            temp.append(-abs(nums1[i] - nums2[i]))
        
        k = k1+k2
        dic = dict(collections.Counter(temp))
        heap = []
        for key in dic:
            heappush(heap, [key, dic[key]])
        
        while len(heap)>1 and k>0:
            
            x = heappop(heap)
            y = heappop(heap)
            
            diff = y[0] - x[0]
            
            if k >= diff*x[1]:
                heappush(heap, [y[0], y[1]+x[1]])
                k -= diff*x[1]
            
            else:
                heappush(heap, y)
                curr_val = -x[0]
                new_val = math.ceil((curr_val*x[1] -k)/x[1])
                t = curr_val - new_val
                k -= t*x[1]
        
                heappush(heap, [-(new_val), x[1]-k])
                heappush(heap, [-(new_val-1), k])
                k = 0
        

        if k>0:
            x = heappop(heap)
            curr_val = -x[0]
            new_val = math.ceil((curr_val*x[1] -k)/x[1])
            t = curr_val - new_val
            k -= t*x[1]
            heappush(heap, [-(new_val), x[1]-k])
            heappush(heap, [-(new_val-1), k])
            k = 0

        
        res = 0
        for i,j in heap:
            if i<0:
                res += (i**2)*j
        return res
            
                
                
        
        
                