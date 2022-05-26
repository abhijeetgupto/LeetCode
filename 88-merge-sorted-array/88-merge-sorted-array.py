class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = n+m-1
        
        idx_nums1 = m-1
        idx_nums2 = n-1
        
        while i>=0 and idx_nums1>=0 and idx_nums2>=0:
            
            if nums1[idx_nums1] > nums2[idx_nums2] :
                nums1[i] = nums1[idx_nums1]
                i-=1
                idx_nums1 -= 1
                
            else:
                nums1[i] = nums2[idx_nums2]
                i-=1
                idx_nums2 -= 1
       
        while idx_nums2 >= 0:
            nums1[i] = nums2[idx_nums2]
            i -= 1
            idx_nums2 -= 1

        
        
            
    