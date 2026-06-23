class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        opening="(","[","{"
        closing=")","]","}"
        bracks={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        # print(opening,closing)
        for st in s:
            if(st in opening):
                arr.append(st)
            elif(st in closing):
                # print(arr)
                if(len(arr)):
                    if(arr[-1]==bracks[st]):
                        arr.pop()
                    else:
                        return False
                else:
                    return False
        if(len(arr)):
            return False
        return True