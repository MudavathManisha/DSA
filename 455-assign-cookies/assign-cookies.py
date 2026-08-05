class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i,j=0,0

        c=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                c+=1
                i+=1

                j+=1
            else:
                j+=1
        return c

