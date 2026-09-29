class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1):
            return 1
        elif(n==0):
            return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        f1=1
        f2=1
        for i in range(2,n):
            f1,f2=f2,f1+f2
        return f1 + f2