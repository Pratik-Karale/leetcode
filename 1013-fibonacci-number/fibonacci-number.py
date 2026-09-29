class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1):
            return 1
        # return self.fib(n-1)+self.fib(n-2)
        
        f1=0
        f2=1
        for i in range(2,n):
            f1,f2=f2,f1+f2
        return f1+f2