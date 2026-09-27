class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        bal=0
        ans=[]
        for ch in s:
            if ch=='(':
                if bal>0:
                    ans.append(ch)
                bal+=1
            else:
                bal-=1
                if bal>0:
                    ans.append(ch)
        return "".join(ans)
