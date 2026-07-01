class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i]=1
        
        li=[[]]*(len(nums)+1)

    
        
        for i in dic:
            if len(li[dic[i]])==0:
                li[dic[i]]=[i]
            else:
                li[dic[i]].append(i)

        print(li)

        out=[]
        counter=0
        for j in range(len(li)-1, 0,-1):
            for o in li[j]:
                if counter<k:
                    out.append(o)
                    counter+=1

                else:
                    return out
        return out
                

       

        
            
        
        