class NumArray:

    def __init__(self, nums: List[int]):
        
        self.n = len(nums)
        tree = [None for _ in range(4*len(nums))]
        
        def build(i=0, left=0, right=len(nums)-1) :
            
            if left>right :
                return 
            
            if left == right :
                tree[i] = nums[left]
                return 
            
            mid = (left+right)//2
            build(2*i+1, left, mid)
            build(2*i+2, mid+1, right)
            tree[i] = tree[2*i+1] + tree[2*i+2]
            return
        
        build()
        self.tree = tree
        
    def update(self, index: int, val: int) -> None:
        
        def modify(i=0, left=0, right=self.n-1) :
            
            if left > right or index < left or index > right :
                return
            
            if  left == right == index :
                self.tree[i] = val
                return 
            
            mid = (left+right)//2
            modify(2*i+1, left, mid)
            modify(2*i+2, mid+1, right)
            self.tree[i] = self.tree[2*i+1] + self.tree[2*i+2]
            return 
        modify()
            
    
    def sumRange(self, left: int, right: int) -> int:
        
        def res(i=0, l=0, r=self.n-1) :
            
            if l>r or left>r or right<l:
                return 0
            
            if l>=left and  r<=right :
                return self.tree[i]
            
            mid = (l+r)//2
            return res(2*i+1, l, mid) + res(2*i+2, mid+1, r)
        
        return res()
            

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)