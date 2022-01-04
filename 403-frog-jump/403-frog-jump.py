class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        
        def rec(arr, j_size, curr_pos, memo = {}) : 
            
            if (curr_pos,j_size) in memo :
                return memo[(curr_pos,j_size)]
            
            if curr_pos == arr[-1] :
                return True
            
            elif j_size <= 0 or curr_pos > arr[-1] :
                return False
            
            else :
                
                j1 = j_size 
                j2 = j_size - 1
                j3 = j_size + 1
                
                fl1 = False
                fl2 = False
                fl3 = False
                
                c1 = curr_pos+j1
                c2 = curr_pos+j2
                c3 = curr_pos+j3
                
                if c1 in arr :
                    if rec(arr,j1,c1,memo) :
                        memo[(c1, j1)] = True
                        fl1 = True
                    else:
                        memo[(c1, j1)] = False
                
                else:
                    memo[(c1,j1)] = False
                
                if c2 in arr :
                    if rec(arr,j2,c2,memo) :
                        memo[(c2, j2)] = True
                        fl2 = True
                    else:
                        memo[(c2, j2)] = False
                
                else:
                    memo[(c2,j2)] = False
                    
                if c3 in arr :
                    if rec(arr,j3,c3,memo) :
                        memo[(c3, j3)] = True
                        fl3 = True
                    else:
                        memo[(c3, j3)] = False
                
                else:
                    memo[(c3,j3)] = False
                
                if fl1 or fl2 or fl3 :
                    memo[(curr_pos,j_size)] = True
                    return True
                
                else:
                    memo[(curr_pos,j_size)] = False
                    return False
                    
        if len(stones)==1 :
            return True
        
        if stones[1] != stones[0]+1 :
            return False
        
        return rec(stones, 1, stones[1])    
                    
                
                
            