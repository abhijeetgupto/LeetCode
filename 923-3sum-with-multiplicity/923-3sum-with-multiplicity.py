class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        dic = dict(collections.Counter(arr))
        keys = sorted(dic.keys())
        
        count = 0
        for i in range(len(keys)) :
            for j in range(i,len(keys)) :
                x = target - keys[i] - keys[j]
                if x >= keys[j] :
                    
                    if keys[i] == keys[j] == x :
                        count += (dic[keys[i]])*(dic[keys[i]]-1)*(dic[keys[i]]-2)//6
                    
                    elif keys[j] == x :
                        count += dic[keys[i]]*(dic[keys[j]])*(dic[keys[j]]-1)//2
                    
                    elif x in dic:
                        if keys[i] == keys[j]:
                            count += dic[x] * (dic[keys[j]]) * (dic[keys[j]] - 1) // 2

                        else:
                            count += dic[keys[i]] * dic[keys[j]] * dic[x]
        return count%(10**9 +7)
                        
                    
                        
                        
        