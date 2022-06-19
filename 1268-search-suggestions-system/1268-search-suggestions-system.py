class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        
        res = []
        products.sort()
        
        for i in range(1, len(searchWord)+1):
            p = []
            flag = False
            for product in products:
                if product[:i] == searchWord[:i]:
                    flag = True
                    p.append(product)
                elif flag:
                    break

            p.sort()
            res.append(p[:3])
            products = p
        
        return res
            
        