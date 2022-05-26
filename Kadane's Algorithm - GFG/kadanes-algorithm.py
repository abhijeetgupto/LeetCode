#User function Template for python3

class Solution:

    def maxSubArraySum(self,arr,n):
        
        res = -math.inf
        curr = 0
        for i in range(n):
            curr += arr[i]
            res = max(res, curr)
            if curr<=0:
                curr=0
        return res
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends