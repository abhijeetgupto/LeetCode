class Solution:
    def compareVersion(self, s1: str, s2: str) -> int:
        
        l1 = s1.split('.')
        l2 = s2.split('.')
        i=j=0
        n1 = len(l1)
        n2 = len(l2)
        flag = None
        
        while i<n1 and j<n2 :
            
            if int(l1[i]) > int(l2[j]) :
                flag = 1
                break
            
            elif int(l1[i]) < int(l2[j]) :
                flag = -1
                break
            
            else:
                i+=1
                j+=1
                
        if flag is not None :
            return flag
        
        if i == n1 :
            for x in range(j,n2) :
                if int(l2[x])!=0:
                    return -1
            return 0
        if j == n2 :
            for x in range(i,n1) :
                if int(l1[x])!=0:
                    return 1
            return 0
            
