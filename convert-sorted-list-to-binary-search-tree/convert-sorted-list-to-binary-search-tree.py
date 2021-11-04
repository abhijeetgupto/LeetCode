class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def helper(arr):
            
            if not arr :
                return 
            
            else:
                m = len(arr)//2
                root = TreeNode(arr[m])
                root.left = helper(arr[ :m])
                root.right = helper(arr[m+1 :])
                return root
        
         
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        arr.sort()
        return helper(arr)

            
            
            
            
        
        