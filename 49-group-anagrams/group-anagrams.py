class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grp={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in grp:
                grp[key]=[]
            grp[key].append(word)
        return list(grp.values())
        