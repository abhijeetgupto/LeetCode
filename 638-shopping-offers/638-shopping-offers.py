class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        memo = {}
        def rec(needs = needs):
            
            x = tuple(needs)
            if  x in memo:
                return memo[x]
            
            if sum(needs) == 0:
                return 0
            
            count = 0
            for i in range(n):
                count += needs[i]*price[i]
            
#             if any(needs[i] < mini[i] for i in range(n)):
#                 return count
            
            res = count

            for offer in special:
                if all(needs[i] >= offer[i] for i in range(n)):
                    temp = [needs[i] - offer[i] for i in range(len(needs))]
                    res = min(res, offer[-1] + rec(temp))
            
            memo[x]  = res       
            return res

        
        n = len(price)
        # mini = [51]*n
        # for offer in special:
        #     for i in range(n):
        #         mini[i] = min(mini[i], offer[i])
        
   
        return rec()