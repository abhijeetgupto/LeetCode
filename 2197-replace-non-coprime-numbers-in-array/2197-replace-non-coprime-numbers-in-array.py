class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
         
        stack = [nums[0]]
        
        for i in range(1,len(nums)):
            
            if math.gcd(stack[-1], nums[i]) > 1 :
                num1 = nums[i]
                
                while math.gcd(num1,stack[-1])>1 :
                    x = math.lcm(num1,stack[-1])
                    stack.pop()
                    if stack :
                        num1 = x
                    else:
                        break
                stack.append(x)
            else:
                stack.append(nums[i])
                
        return stack
                    
                    

                
                
                
            
            
        
        
                
                
        
        