class Solution:
    def isPalindrome(self, s: str) -> bool:
        # st=[]
        # for c in s:
        #     if(c.upper()!=c.lower() or c in):
        #         st.append(c.lower())
        # s="".join(st)
        a=0
        b=len(s)-1
        while(a<b):
            if(not s[a].isalnum()):
                a+=1
                continue
            elif(not s[b].isalnum()):
                b-=1
                continue
            if(s[a].lower()!=s[b].lower()):
                return False
            a+=1
            b-=1
        return True
            