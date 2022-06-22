class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pivot = random.choice(nums)
        greater = [x for x in nums if x>pivot]
        less = [x for x in nums if x<pivot]
        equal = [x for x in nums if x==pivot]
        
        if k <= len(greater):
            return self.findKthLargest(greater, k)
        
        elif k > len(greater) + len(equal):
            return self.findKthLargest(less, k - len(greater) - len(equal))
        
        else:
            return equal[0]
            