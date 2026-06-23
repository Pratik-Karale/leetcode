class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=[]
        for c in s:
            if(c.upper()!=c.lower() or c in "1234567890"):
                st.append(c.lower())
        a=0
        b=len(st)-1
        while(a<=b):
            if(st[a]!=st[b]):
                return False
            a+=1
            b-=1
        return True
            