class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums2 = nums2   
        self.dic1 = dict(collections.Counter(nums1))
        self.dic2 = dict(collections.Counter(nums2))

    def add(self, index: int, val: int) -> None:
        
        key = self.nums2[index]
        self.nums2[index] += val
        
        if self.dic2[key] == 1 :
            self.dic2.pop(key)
        else :
            self.dic2[key] -= 1
        
        if key+val in self.dic2 :
            self.dic2[key+val] += 1
        else:
            self.dic2[key+val] = 1


    def count(self, tot: int) -> int:
        
        count = 0
        for num in self.dic1 :
            x = tot-num
            if x in self.dic2 :
                count += self.dic1[num]*self.dic2[x]
        
        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)