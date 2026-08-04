class Solution:
    def addDigits(self, num: int) -> int:
        ournum=num
        while ournum>9:
            sum=0
            for n in str(ournum):
                sum+=int(n)
            ournum=sum
        return ournum