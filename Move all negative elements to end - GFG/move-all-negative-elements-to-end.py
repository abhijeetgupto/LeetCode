#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        
        positive = []
        negative = []
        for num in arr:
            if num<0:
                negative.append(num)
            else:
                positive.append(num)
        arr[:] = positive+negative
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends