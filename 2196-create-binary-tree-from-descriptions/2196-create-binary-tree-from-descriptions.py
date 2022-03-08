# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        dic = {}
        childrens = set()
        
        
        for parent,child,left in descriptions :
            
            childrens.add(child)
            
            if parent not in dic : 
                dic[parent] = TreeNode(parent)
            
            if child not in dic :
                dic[child] = TreeNode(child)
  
            if left == 0:
                dic[parent].right = dic[child]
            else:
                dic[parent].left = dic[child]
                    
        
        roots = set(dic.keys())
        
        for node in roots :
            if node not in childrens :
                return dic[node]
            
            
                    
                
        