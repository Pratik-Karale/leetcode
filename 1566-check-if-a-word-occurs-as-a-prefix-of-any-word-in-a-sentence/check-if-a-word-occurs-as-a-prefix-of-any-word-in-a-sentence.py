class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        w=1
        c=0
        for s in range(len(sentence)):
            if(sentence[s]==" "):
                w+=1
                c=0
                continue
            elif(c==-1):
                continue
            if(sentence[s]==searchWord[c]):
                c+=1
                if(c==len(searchWord)):
                    return w
            elif(sentence[s]!=searchWord[c]):
                c=-1
        return -1