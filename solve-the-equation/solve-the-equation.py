class Solution:
    def solveEquation(self, equation: str) -> str:

        def x(left):
            x_left = 0
            for i in range(len(left)) :
                if left[i] == 'x' :
                    temp = ""
                    j = i-1
                    while j>=0 :
                        temp += left[j]
                        if temp[-1] == '-' or temp[-1] == '+' :
                            break
                        j -= 1

                    if not temp or temp == '+':
                        x_left += 1

                    elif temp == '-' :
                        x_left -= 1
                    
                    elif '+' not in temp and '-' not in temp :
                        x_left += int(temp)

                    else:
                        temp = temp[::-1]
                        if temp[0] == '-' :
                            x_left -= int(temp[1:])
                        else:
                            x_left += int(temp[1:])
            return x_left
        
        def val(s) : 
            c=''
            for char in s :
                if char == "-":
                    c += '+'
                c += char
            l = c.split('+')

            val = 0
            for i in range(len(l)):
                try :
                    val += int(l[i])
                except:
                    pass
            return val

        left,right = equation.split('=')

        x_left = x(left)
        x_right = x(right)
        
        val_left = val(left)
        val_right = val(right)
        

        if x_left == x_right and val_left == val_right :
            return "Infinite solutions"
        
        elif x_left == x_right  :
            return "No solution"
        
        else:
            if x_left > x_right :
                temp1 = x_left-x_right
                temp2 = val_right-val_left
                x = math.gcd(temp1,abs(temp2))
                temp1 = temp1//x
                temp2 = temp2//x
                
                if temp1 == 1:
                    return  "x=" + str(temp2)
                
                else:
                    return str(temp1) + "x=" + str(temp2)
   
            else:
                temp1 = x_right-x_left
                temp2 = val_left-val_right
                x = math.gcd(temp1,abs(temp2))
                temp1 = temp1//x
                temp2 = temp2//x
                
                if temp1 == 1:
                    return  "x=" + str(temp2)
                
                else:
                    return str(temp1) + "x=" + str(temp2)
        
               
                           
    
                    
                
        
        
        