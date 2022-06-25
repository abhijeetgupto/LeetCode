class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        def checker(changed = False):
            
            curr_max = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[curr_max]:
                    if changed:
                        return False
                    else:
                        
                        if curr_max == 0:
                            temp = nums[curr_max]
                            nums[curr_max] = -100000
                            
                        else:
                            temp = nums[curr_max]
                            nums[curr_max] = nums[curr_max-1]
                            
                        a = checker(True)
                        if a :return True
                        nums[curr_max] = temp
                        nums[i] = nums[curr_max]
                        b = checker(True)
                        return a or b
                curr_max = i
                
            return True
                            

        

        return checker()
        