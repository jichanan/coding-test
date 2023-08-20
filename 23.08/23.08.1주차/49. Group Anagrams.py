class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        tem = {}

        for s in strs:
            sort_s = ''.join(sorted(s))
            if sort_s in tem:
                tem[sort_s].append(s)
            else:
                tem[sort_s] = [s]

        return list(tem.values())
