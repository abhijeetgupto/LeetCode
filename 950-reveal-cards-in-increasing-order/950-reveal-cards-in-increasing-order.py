class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort(reverse = True)
        n = len(deck)
        i = 0
        res = [None]*len(deck)
        last = len(deck)%2==0
        
        while i<n:
            res[i] = deck.pop()
            i += 2
        
        while deck:
            if last:
                flag = True
                for i in range(n):
                    if res[i] is None:
                        if flag:
                            res[i] = deck.pop()
                            flag = False
                        else:
                            flag = True
            else:
                flag = False
                for i in range(n):
                    if res[i] is None:
                        if flag:
                            res[i] = deck.pop()
                            flag = False
                        else:
                            flag = True
            last = flag
        return res
                
            
                
                
                
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(deck)
#         deck.sort(reverse=True)
#         res = [0]*n
#         l = list(range(n))
#         last = None
        
#         while deck :
            
#             if last is None :
#                 temp = []
#                 for i in range(len(l)) :
#                     if i%2==0:
#                         res[l[i]] = deck.pop()
#                     else:
#                         temp.append(l[i])
#                 l = temp
#                 if n%2 == 0:
#                     last = "e"
#                 else:
#                     last = "o"
                    
                    
#             else:
#                 if last == 'e' :
#                     temp = []
#                     for i in range(len(l)) :
#                         if i%2==0:
#                             res[l[i]] = deck.pop()
#                         else:
#                             temp.append(l[i])
                    
#                     if len(l)%2 == 0 :
#                         last = 'e'
#                     else:
#                         last = 'o'
#                     l = temp
                    
#                 else:
#                     if len(l)%2 == 0:
#                         temp = []
#                         for i in range(len(l)) :
#                             if i%2!=0:
#                                 res[l[i]] = deck.pop()
#                             else:
#                                 temp.append(l[i])
#                         if len(l)%2==0:
#                             last = 'e'
#                         else:
#                             last = 'o'
#                         l = temp
                    
#                     else:
#                         temp = []
#                         for i in range(len(l)) :
#                             if i%2==0:
#                                 res[l[i]] = deck.pop()
#                             else:
#                                 temp.append(l[i])

#                         if len(l)%2 == 0 :
#                             last = 'e'
#                         else:
#                             last = 'o'
        
#         return res
                        
                        
                        
                    

                        
                        
            
            
        