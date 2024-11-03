class Solution {
    bool hasOnlyCapOrLow(string sentence){
        bool firstIsUpper=isupper(sentence[0]);
        cout<<"First "<<firstIsUpper;
        for(int i = 1;i<sentence.length();i++){
            bool currIsUpper=isupper(sentence[i]);
            cout<<"\n"<<i<<" "<<currIsUpper;
            if(firstIsUpper != currIsUpper){
                return false;
            }
        }
        return true;
    }
    bool hasConnectedWords(string sentence){
        char last;
        bool prevWasSpace=false;
        for(int i=0;i<sentence.length();i++){
            if(sentence[i]!=last && prevWasSpace){
                return false;
            }
            if(sentence[i]==' ' && i>0 && sentence[i-1]!=' '){
                    prevWasSpace=true;
                    last=sentence[i-1];
            }
            else prevWasSpace=false;
        }
        return true;
    }
public:
    bool isCircularSentence(string sentence) {
        if(sentence.length()<1 || sentence.length()>500) return false;
        char first=sentence[0];
        char last=sentence[sentence.length()-1];
        if(first==' ' || last==' ') return false;
        if(first!=last)return false;
        // if(!hasOnlyCapOrLow(sentence))return false;
        if(!hasConnectedWords(sentence))return false;
        return true;
    }
};