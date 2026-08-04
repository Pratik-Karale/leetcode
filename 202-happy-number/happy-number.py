class Solution:
    def isHappy(self, n: int) -> bool:
        st=set()
        ournum=n
        while ournum!=1:
            sum=0
            for i in str(ournum):
                sum+=(int(i)**2)
                # print(sum,int(i)**2,int(i))
            if(sum in st):
                return False
            ournum=sum
            st.add(ournum)
        return True