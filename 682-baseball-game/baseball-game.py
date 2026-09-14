class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        ops=operations
        for i in range(len(operations)):
            if ops[i]=='+':
                res.append(res[len(res)-2]+res[len(res)-1])
            elif ops[i]=='D':
                res.append(res[len(res)-1]*2)
            elif ops[i]=='C':
                res.pop()
            else:
                res.append(int(ops[i]))
        return sum(res)
                