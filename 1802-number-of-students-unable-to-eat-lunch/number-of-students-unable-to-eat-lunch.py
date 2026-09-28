class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # tp=0
        # st=0
        # i=0
        # while(tp!=len(sandwiches) or i!=len(sandwiches)-tp):
        #     if(sandwiches[tp]==students[st]):
        #         students[st]=-1
        #         tp+=1
        #         st+=1
        #         continue
        #     else:
        #         if(st>=len(students)):
        #             st=0
        #             i=0
        #         else:
        #             st+=1
        #             i+=1
        
        #     return len(sandwiches)-tp
        st=0
        for sandwich in sandwiches:
            ini=len(students)-1 if st==0 else st-1
            while(sandwich!=students[st] and ini!=st):
                st+=1
                if(st==len(students)):
                    st=0
                    continue
            if(ini==st and sandwich!=students[st]):
                break
            students[st]=-1
        return sum([0 if no==-1 else 1 for no in students])

            