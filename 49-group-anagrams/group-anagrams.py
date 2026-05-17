class Solution:
    def isAnagram(self,s,t):
        if(len(s)!=len(t)): return False
        map=[0]*26
        def get_i(char):
            return ord(char)-ord("a")

        for char in s:
            map[get_i(char)]+=1
        for char in t:
            if(map[get_i(char)]!=0):
                map[get_i(char)]-=1
            else:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        print(self.isAnagram("nat","atn"))
        print(self.isAnagram("nat","att"))
        for i in range(len(strs)):
            isAppended=False
            for word in map:
                if(self.isAnagram(word,strs[i])):
                    map[word].append(strs[i])
                    isAppended=True
                    break
            if(not isAppended):
                map[strs[i]]=[strs[i]]
        
        op=[]
        for word in map:
            op.append(map[word])
        return op


        