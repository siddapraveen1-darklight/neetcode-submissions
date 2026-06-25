class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = {}
        for i in strs:
            li=[0]*26
            for j in i:
                li[ord(j)-97]+=1
            print(li)
            st=""
            for k in li:
                if k==0:
                    st+="*";
                else:
                    k=""+str(k)
                    st+=k
                    st+="*"
            if st in hm:
                prev = hm[st]
                prev.append(i)
                hm[st]=prev
            else:
                hm[st]=[i]
        out=[]
        for i in hm:
            out.append(hm[i])
        return out
        


        
        