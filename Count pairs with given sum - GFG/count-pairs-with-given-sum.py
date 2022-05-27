#User function Template for python3
import collections
class Solution:
    def getPairsCount(self, arr, n, k):
        
        dic = collections.Counter(arr)
        count = 0
        
        for num in set(arr):
            temp = k-num
            if temp==num:
                count += (dic[num])*(dic[num]-1)//2
            
            elif temp>num and temp in dic:
                count += dic[num]*dic[temp]
        return count
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends