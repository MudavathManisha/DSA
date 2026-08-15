class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        start,end=intervals[0]
        for i in range(1,len(intervals)):
            new_start,new_end=intervals[i]
            if new_start<=end:
                end=max(end,new_end)
            else:
                res.append([start,end])
                start=new_start
                end=new_end
        res.append([start,end])
        return res





        