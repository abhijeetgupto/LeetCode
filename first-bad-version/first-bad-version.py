# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 1
        u = n
        if l==u:
            return 1
        while l <= u :
            mid = (l+u)//2
            
            if isBadVersion(mid) :
                if not isBadVersion(mid-1):
                    return mid
                u = mid-1        
            else :
                l = mid+1