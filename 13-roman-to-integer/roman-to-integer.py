class Solution:
    def romanToInt(self, s: str) -> int:
        mp={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        wm={
            "I":None,
            "V":"I",
            "X":"I",
            "L":"X",
            "C":"X",
            "D":"C",
            "M":"C"
        }
        sum=mp[s[0]]
        for i in range(1,len(s)):
            c=s[i]
            if(wm[c] and s[i-1]==wm[c]):
                sum-=mp[wm[c]]*2
            sum+=mp[c]
        return sum      
