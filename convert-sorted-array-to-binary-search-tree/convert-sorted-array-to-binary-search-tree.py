# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(arr):
            
            if not arr :
                return 
            
            else:
                m = len(arr)//2
                root = TreeNode(arr[m])
                root.left = helper(arr[ :m])
                root.right = helper(arr[m+1 :])
                return root

        return helper(nums)